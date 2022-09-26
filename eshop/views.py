from django.shortcuts import render, redirect, reverse, get_object_or_404
from portfolio.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def add_tutorial(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial added successfully!')
            return redirect(reverse('tutorial_detail', args=[tutorial.id]))
        else:
            messages.error(request, 'Failed to add the tutorial, Please ensure that the form is valid!')
    else:
        form = TutorialForm()
    template = 'eshop/add_tutorial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_tutorial(request, tutorial_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial updated successfully!')
            return redirect(reverse('tutorial_detail', args=[tutorial.id]))
        else:
            messages.error(request, 'Failed to update the tutorial, Please ensure that the form is valid!')
    else:
        form = TutorialForm(instance=tutorial)
        messages.info(request, f'You are editing {tutorial.title}')

    template = 'eshop/edit_tutorial.html'
    context = {
        'form': form,
        'tutorial': tutorial,
    }
    return render(request, template, context)

@login_required
def delete_tutorial(request, tutorial_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    tutorial.delete()
    messages.success(request, 'Tutorial deleted')
    return redirect(reverse('tutorials'))