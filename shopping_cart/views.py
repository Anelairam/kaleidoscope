from django.shortcuts import render, redirect

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, photo_id):
    
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if photo_id in list(cart.keys()):
        print('Item exists')
    else:
        cart[photo_id] = photo_id

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
