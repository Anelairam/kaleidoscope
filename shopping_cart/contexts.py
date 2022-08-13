from django.shortcuts import get_object_or_404
from portfolio.models import Photo

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    # for photo_id, photo_id in cart.items():
    #     photo = get_object_or_404(Photo, pk=photo_id)
    #     total += photo.price
    #     item_count += 1
    #     cart_items.append({
    #         'photo_id': photo_id,
    #         'photo': photo,
    #     })

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context