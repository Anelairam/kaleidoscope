from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    products = Product.objects.all()
    query = None
    labels = None

    if request.GET:
        if 'label' in request.GET:
            labels = request.GET['label'].split(',')
            photos = photos.filter(label__name__in=labels)
            labels = Category.objects.filter(name__in=labels)

            
            queries = Q(label__icontains=query) | Q(location__icontains=query)
            photos = photos.filter(queries)

    context = {
        'products': products,
        'search_item': query,
        'current_label': labels,
    }

    return render(request, 'portfolio/portfolio.html', context)


def product_detail(request, product_id):
    """The view returns the index page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'portfolio/product_detail.html', context)