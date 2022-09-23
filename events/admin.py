from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'day',
        'starting_at',
        'ending_at',
        'description',
    )


admin.site.register(Event, EventAdmin)