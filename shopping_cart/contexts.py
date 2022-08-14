from django.shortcuts import get_object_or_404
from portfolio.models import Product
# from portfolio.models import Photo

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    

    grand_total = total

    context = {
        'cart_items': cart_items,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context