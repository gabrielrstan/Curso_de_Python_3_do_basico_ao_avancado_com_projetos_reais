from django.contrib import messages  # type: ignore
from django.shortcuts import redirect  # type: ignore
from django.urls import reverse  # type: ignore
from django.views import View  # type: ignore
from django.views.generic import DetailView, ListView  # type: ignore

from order.models import Order, OrderedItem
from product.models import Variation
from utils.utils import cart_total_price, cart_total_quantity


class DispatchLoginRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('user:create')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()  # type: ignore
        qs = qs.filter(user=self.request.user)
        return qs


class Pay(DispatchLoginRequiredMixin, DetailView):
    template_name = 'order/pay.html'
    model = Order
    pk_url_kwarg = 'pk'
    context_object_name = 'order'


class SaveOrder(View):
    template_name = 'order/pay.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Você precisa estar logado.')
            return redirect('user:create')

        if not self.request.session.get('cart'):
            messages.error(self.request, 'Carrinho vazio.')
            return redirect('product:list')

        cart = self.request.session.get('cart')
        cart_variation_id = [v for v in cart]  # type:ignore
        variation_db = list(Variation.objects.select_related('product')
                            .filter(id__in=cart_variation_id))

        for variation in variation_db:
            vid = str(variation.id)  # type: ignore
            stock = variation.stock
            amount_in_cart = cart[vid]['quantity']  # type: ignore
            unit_price = cart[vid]['unit_price']  # type: ignore

            # type: ignore noqa: E501
            promotional_unit_price = (cart[vid]  # type: ignore
                                      ['promotional_unit_price'])

            stock_msg_error = ''

            if stock < amount_in_cart:
                cart[vid]['quantity'] = stock  # type: ignore
                cart[vid]['quantitative_price'] = (unit_price *  # type: ignore
                                                   stock)
                cart[vid]['promotional_quantitative_price'] = (stock *  # noqa E501 # type: ignore
                                                               promotional_unit_price)  # noqa E501

                stock_msg_error = ('Estoque insuficiente para alguns produtos '
                                   'do seu carrinho. Foi reduzido a quantidade'
                                   ' destes produtos. Verifique quais produtos'
                                   ' foram afetados'
                                   )

            if stock_msg_error:
                messages.error(self.request, stock_msg_error)

                self.request.session.save()

                return redirect('product:cart')

        total_amount_cart = cart_total_quantity(cart)
        total_valor_cart = cart_total_price(cart)

        order = Order(
            user=self.request.user,
            total=total_valor_cart,
            total_amount=total_amount_cart,
            status='C',
        )

        order.save()

        OrderedItem.objects.bulk_create(
            [
                OrderedItem(
                    order=order,
                    product=v['product_name'],
                    product_id=v['product_id'],
                    variation=v['variation_name'],
                    variation_id=v['variation_id'],
                    price=v['quantitative_price'],
                    promotional_price=v['promotional_quantitative_price'],
                    quantity=v['quantity'],
                    image=v['image'],
                ) for v in cart.values()  # type: ignore

            ]
        )

        del self.request.session['cart']
        return redirect(
            reverse(
                'order:pay',
                kwargs={
                    'pk': order.pk,
                }
            )
        )


class Detail(DispatchLoginRequiredMixin, DetailView):
    template_name = 'order/detail.html'
    model = Order
    context_object_name = 'order'
    pk_url_kwargs = 'pk'


class List(DispatchLoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'order/list.html'
    paginate_by = 10
    ordering = ['-id']
