from django import template


register = template.Library()

@register.filter(name='subtotal_calcution')
def subtotal_calcution(price, quantity):
    return price * quantity