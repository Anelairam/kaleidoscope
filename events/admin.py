from django.contrib import admin
from .models import Event, Difficulty

# Register your models here.

class DifficultyAdmin(admin.ModelAdmin):
    list_display = (
        'difficulty',
    )


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'day',
        'difficulty',
        'starting_at',
        'ending_at',
        'description',
    )


admin.site.register(Difficulty, DifficultyAdmin)
admin.site.register(Event, EventAdmin)
