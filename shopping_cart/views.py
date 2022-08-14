from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from portfolio.models import Product

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    try:
        cart = request.session.get('cart', {})
        cart.pop(product_id)
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)

