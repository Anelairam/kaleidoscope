from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from .forms import ProductForm


# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    products = Product.objects.all()
    category = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'portfolio/portfolio.html', context)


def product_detail(request, product_id):
    """The view returns the index page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'portfolio/product_detail.html', context)


def add_product(request):
    form = ProductForm()
    template = 'portfolio/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)