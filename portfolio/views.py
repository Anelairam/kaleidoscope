from django.shortcuts import render
from .models import Photo

# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'portfolio/portfolio.html', context)