from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse, get_object_or_404  # type: ignore
from django.views.generic.list import ListView  # type: ignore
from django.views.generic.detail import DetailView  # type: ignore
from django.views import View  # type: ignore
from django.contrib import messages  # type: ignore
from product.models import Product, Variation


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 10


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
        id_variation = self.request.GET.get('vid')

        if not id_variation:
            messages.error(
                self.request,
                'Product does not exist'
            )
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=id_variation)

        if not self.request.session.get('cart'):
            self.request.session['cart'] = {}
            self.request.session.save()

        cart = self.request.session['cart']

        if id_variation in cart:
            pass
        else:
            pass

        return HttpResponse(f'{variation.name} {variation.product}')


class RemoveFromCart(View):
    ...


class Cart(View):
    ...


class Finish(View):
    ...
