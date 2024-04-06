# from django.shortcuts import render  # type: ignore
from django.views.generic.list import ListView  # type: ignore
from django.views import View  # type: ignore


class ProductList(ListView):
    ...


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
