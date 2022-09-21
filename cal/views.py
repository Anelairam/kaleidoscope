from django.shortcuts import render

# Create your views here.
def events_calendar(request):
    """The view returns the index page"""
    return render(request, 'cal/calendar.html')