from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'starting_time',
        'ending_time',
    )



admin.site.register(Event, EventAdmin)