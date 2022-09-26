from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
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


@login_required
def add_event(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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

@login_required
def edit_event(request, event_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 'Failed to update the event, Please ensure that the form is valid!')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }
    return render(request, template, context)

@login_required
def delete_event(request, event_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted')
    return redirect(reverse('events'))