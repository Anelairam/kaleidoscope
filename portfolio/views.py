from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Photo

# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    photos = Photo.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Not such information')
                return redirect(reverse('portfolio'))
            
            queries = Q(label__icontains=query) | Q(location__icontains=query)
            photos = photos.filter(queries)

    context = {
        'photos': photos,
        'search_item': query
    }

    return render(request, 'portfolio/portfolio.html', context)


def photo_detail(request, photo_id):
    """The view returns the index page"""
    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photos': photo,
    }

    return render(request, 'portfolio/photo_detail.html', context)