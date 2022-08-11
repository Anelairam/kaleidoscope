from django.shortcuts import render

# Create your views here.

def cart(request):
    """The view returns the index page"""
    return render(request, 'shopping_cart/cart.html')