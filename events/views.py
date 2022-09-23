from django.shortcuts import render
from .models import Event


# Create your views here.
def events(request):
    """The view returns the index page"""
    events = Event.objects.all()
    context= {
        'events': events,
    }
    return render(request, 'events/events.html', context)