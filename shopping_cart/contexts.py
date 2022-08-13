from django.shortcuts import get_object_or_404
from portfolio.models import Product
# from portfolio.models import Photo

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for product_id in cart.items():
        print('Hello',cart_items)
        # product = get_object_or_404(Product, pk=product_id)
        # total += product.price
        # item_count += 1
        cart_items.append({
            'product_id': product_id,
            # 'product': product,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context