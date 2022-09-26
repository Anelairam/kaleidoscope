from django.shortcuts import render, redirect, reverse
from portfolio.models import Product
from django.contrib import messages

from .models import Tutorial
from .forms import TutorialForm

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


def add_tutorial(request):

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial added successfully!')
            return redirect(reverse('add_tutorial'))
        else:
            messages.error(request, 'Failed to add the tutorial, Please ensure that the form is valid!')
    else:
        form = TutorialForm()
    template = 'eshop/add_tutorial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)