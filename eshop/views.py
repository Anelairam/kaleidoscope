from django.shortcuts import render
from .models import OnlineCourse, Tour

# Create your views here.

def eshop(request):
    """The view returns the index page"""
    online_courses = OnlineCourse.objects.all()
    tours = Tour.objects.all()

    context = {
        'onlinecourses': online_courses,
        'tours': tours,
    }
    return render(request, 'eshop/eshop.html', context)