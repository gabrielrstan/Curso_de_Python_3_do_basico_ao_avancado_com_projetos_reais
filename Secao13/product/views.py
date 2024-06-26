
from django.contrib import messages  # type: ignore
from django.db.models import Q  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore  # noqa - E501
from django.shortcuts import redirect, render
from django.urls import reverse  # type: ignore
from django.views import View  # type: ignore
from django.views.generic.detail import DetailView  # type: ignore
from django.views.generic.list import ListView  # type: ignore

from product.models import Product, Variation
from user.models import Profile


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 10
    ordering = ['-id']


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class AddToCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:list')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.id  # type:ignore
        product_name = product.name
        variation_name = variation.name or ''
        unit_price = variation.price
        promotional_unit_price = variation.promotional_price
        quantity = 1  # noqa - F841
        slug = product.slug
        image = product.image

        if image:
            image = image.name
        else:
            image = ''

        if variation.stock < 1:
            messages.error(self.request, 'Produto em falta no estoque')
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if variation_id in cart:
            cart_quantity = cart[variation_id]['quantity']
            cart_quantity += 1

            if variation_stock < cart_quantity:
                messages.warning(
                    self.request,
                    f'Estoque insuficiente para {cart_quantity}x '
                    f'no produto "{product_name}". Adicionamos '
                    f'{variation_stock}x no seu carrinho.'
                )
                cart_quantity = variation_stock

            cart[variation_id]['quantity'] = cart_quantity
            cart[variation_id]['quantitative_price'] = unit_price * \
                cart_quantity
            cart[variation_id]['promotional_quantitative_price'] = promotional_unit_price * cart_quantity  # noqa - E501
        else:
            cart[variation_id] = {
                'product_id': product_id,
                'product_name': product_name,
                'variation_name': variation_name,
                'variation_id': variation_id,
                'unit_price': unit_price,
                'promotional_unit_price': promotional_unit_price,
                'quantitative_price': unit_price,
                'promotional_quantitative_price': promotional_unit_price,
                'quantity': 1,
                'slug': slug,
                'image': image,
            }
        self.request.session.save()

        messages.success(
            self.request,
            f'Adicionado o produto "{product_name} {variation_name}" ao '
            'seu Carrinho.'
            f' Quantidade: {cart[variation_id]["quantity"]}x.'
        )

        return redirect(http_referer)


class RemoveFromCart(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('product:cart')
        )
        variation_id = self.request.GET.get('vid')

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get('cart'):
            return redirect(http_referer)

        if variation_id not in self.request.session['cart']:
            return redirect(http_referer)

        cart = self.request.session['cart'][variation_id]

        messages.success(
            self.request,
            f'Removido {cart["product_name"]} {cart["variation_name"]} '
            f'do seu carrinho.'
        )

        del self.request.session['cart'][variation_id]
        self.request.session.save()
        return redirect(http_referer)


class Cart(View):
    def get(self, *args, **kwargs):
        context = {
            'cart': self.request.session.get('cart', {}),
        }
        return render(self.request, 'product/cart.html', context)


class PurchaseSummary(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('user:create')

        profile = Profile.objects.filter(user=self.request.user).exists()

        if not profile:
            messages.error(
                self.request,
                'Você precisa criar adicionar um perfil ao usuário.'
            )
            return redirect('user:create')

        if not self.request.session.get('cart'):
            messages.error(
                self.request,
                'Você precisa adicionar um produto ao seu carrinho.'
            )
            return redirect('product:list')

        context = {
            'user': self.request.user,
            'cart': self.request.session['cart'],
        }
        return render(self.request, 'product/purchase_summary.html', context)


class Search(ProductList):
    def get_queryset(self, *args, **kwargs):
        term = self.request.GET.get('term') or self.request.session['term']
        qs = super().get_queryset(*args, **kwargs)

        if not term:
            return qs

        self.request.session['term'] = term

        qs = qs.filter(
            Q(name__icontains=term) |
            Q(short_description__icontains=term) |
            Q(long_description__icontains=term)
        )

        self.request.session.save()

        return qs
