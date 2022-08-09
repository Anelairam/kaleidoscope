from django.shortcuts import render

# Create your views here.

def portfolio(request):
    """The view returns the index page"""
    return render(request, 'portfolio/portfolio.html')