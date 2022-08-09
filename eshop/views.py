from django.shortcuts import render

# Create your views here.

def eshop(request):
    """The view returns the index page"""
    return render(request, 'eshop/eshop.html')