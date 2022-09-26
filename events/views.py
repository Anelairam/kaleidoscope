from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from datetime import datetime
from .models import Event
from .forms import EventForm


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



def add_event(request):

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event scheduled successfully!')
            return redirect(reverse('add_event'))
        else:
            messages.error(request, 'Failed to schedule the event, Please ensure that the form is valid!')
    else:
        form = EventForm()
    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)