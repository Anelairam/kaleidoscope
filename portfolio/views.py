from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from eshop.models import OnlineCourse, Tour
from .models import Photo, Category


# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    photos = Photo.objects.all()
    query = None
    labels = None

    if request.GET:
        if 'label' in request.GET:
            labels = request.GET['label'].split(',')
            photos = photos.filter(label__name__in=labels)
            labels = Category.objects.filter(name__in=labels)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Not such information')
                return redirect(reverse('portfolio'))
            
            queries = Q(label__icontains=query) | Q(location__icontains=query)
            photos = photos.filter(queries)

    context = {
        'photos': photos,
        'search_item': query,
        'current_label': labels,
    }

    return render(request, 'portfolio/portfolio.html', context)


def photo_detail(request, photo_id):
    """The view returns the index page"""
    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'portfolio/photo_detail.html', context)


def onlinecourse_detail(request, onlinecourse_id):
    """The view returns the index page"""
    onlinecourse = get_object_or_404(OnlineCourse, pk=onlinecourse_id)

    context = {
        'onlinecourse': onlinecourse,
    }

    return render(request, 'portfolio/onlinecourse_detail.html', context)


def tour_detail(request, tour_id):
    """The view returns the index page"""
    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'portfolio/tour_detail.html', context)