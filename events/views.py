from django.shortcuts import render
from datetime import datetime
from .models import Event


# Create your views here.
def events(request):
    """The view returns the index page"""
    events = Event.objects.all()
    today = datetime.now()
    current_month = today.month

    context= {
        'events': events,
        'current_month': current_month,
    }
    return render(request, 'events/events.html', context)