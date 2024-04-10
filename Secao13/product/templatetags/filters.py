from django.template import Library  # type: ignore
from utils import utils

register = Library()


@register.filter
def format_price(value):
    return utils.format_price(value)


@register.filter
def cart_total_quantity(cart):
    return utils.cart_total_quantity(cart)


@register.filter
def cart_total_price(cart):
    return utils.cart_total_price(cart)
