from django.shortcuts import get_object_or_404
from portfolio.models import Product
# from portfolio.models import Photo

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total += quantity * product.price
        item_count += quantity
        cart_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'item_count': item_count,
        'grand_total': grand_total,
    }

    return context