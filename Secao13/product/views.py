# from django.shortcuts import render  # type: ignore
from django.views.generic.list import ListView  # type: ignore
from django.views import View  # type: ignore
from product.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 10


class ProductDetail(View):
    ...


class AddToCart(View):
    ...


class RemoveFromCart(View):
    ...


class Cart(View):
    ...


class Finish(View):
    ...
