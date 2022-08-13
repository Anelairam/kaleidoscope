from django.shortcuts import render
from .models import OnlineCourse, Tour
from portfolio.models import Photo

# Create your views here.

def eshop(request):
    """The view returns the index page"""
    online_courses = OnlineCourse.objects.all()
    tours = Tour.objects.all()
    photos = Photo.objects.all()

    context = {
        'onlinecourses': online_courses,
        'tours': tours,
        'photos': photos,
    }
    return render(request, 'eshop/eshop.html', context)