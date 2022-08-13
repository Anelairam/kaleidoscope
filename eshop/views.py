from django.shortcuts import render
from portfolio.models import Product

# Create your views here.

def eshop(request):
    """The view returns the index page"""
    products = Product.objects.all()


    context = {
        'products': products,
    }
    return render(request, 'eshop/eshop.html', context)