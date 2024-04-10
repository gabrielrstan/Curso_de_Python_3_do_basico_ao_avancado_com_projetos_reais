def format_price(value):
    return f'R$ {value:.2f}'.replace('.', ',')


def cart_total_quantity(cart):
    return sum([item['quantity'] for item in cart.values()])


def cart_total_price(cart):
    return sum(
        [
            item.get('promotional_quantitative_price')
            if item.get('promotional_quantitative_price')
            else item.get('quantitative_price')
            for item
            in cart.values()
        ]
    )
