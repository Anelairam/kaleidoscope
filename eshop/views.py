from django.shortcuts import render
from portfolio.models import Product
from .models import Tutorial

# Create your views here.

def eshop(request):
    """The view returns the index page"""
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'eshop/eshop.html', context)


def tutorials(request):
    """The view returns the index page"""
    tutorials = Tutorial.objects.all()

    context = {
        'tutorials': tutorials,
    }
    return render(request, 'eshop/tutorials.html', context)