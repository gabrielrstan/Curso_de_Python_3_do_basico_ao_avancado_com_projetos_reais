from django.template import Library  # type: ignore
from utils import utils

register = Library()


@register.filter
def format_price(value):
    return utils.format_price(value)
