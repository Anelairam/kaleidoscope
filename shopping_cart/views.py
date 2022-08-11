from django.shortcuts import render

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')


def add_to_bag(request, item_id):
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    cart[item_id]
