from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_calendar, name='events_calendar'),
    path(r'^calendar/$', views.CalendarView.as_view(), name='events_calendar'), # here
]