from django.contrib import admin
from .models import Tutorial

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'description',
        'price',
    )



admin.site.register(Tutorial, TutorialAdmin)
