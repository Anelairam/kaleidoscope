from django.shortcuts import render

# Create your views here.
def events(request):
    """The view returns the index page"""
    return render(request, 'events/events.html')