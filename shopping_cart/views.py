from django.shortcuts import render, redirect

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, product_id):
    
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})  

    if product_id in list(cart.keys()):
        print('Item exists')
    else:
        print(product_id)
        # cart[product_id] = product_id

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
