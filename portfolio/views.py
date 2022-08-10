from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'portfolio/portfolio.html', context)


def photo_detail(request, photo_id):
    """The view returns the index page"""
    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photos': photo,
    }

    return render(request, 'portfolio/photo_detail.html', context)