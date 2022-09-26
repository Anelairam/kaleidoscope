from django.shortcuts import render

# Create your views here.

def index(request):
    """The view returns the index page"""
    return render(request, 'home/index.html')


def handler_not_found(request, exception):
    """The view returns the custom 404 page"""
    return render(request, 'not_found.html')