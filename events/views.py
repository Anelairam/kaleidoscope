from django.shortcuts import render
from datetime import datetime
from .models import Event


# Create your views here.
def events(request):
    """The view returns the index page"""
    events = Event.objects.all()
    today = datetime.now()

    context = {
        'events': events,
        'today': today,
    }
    return render(request, 'events/events.html', context)