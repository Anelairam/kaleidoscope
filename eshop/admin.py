from django.contrib import admin
from .models import OnlineCourse, Tour
# Register your models here.

class OnlineCourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'description',
        'price',
        'sku',
    )

class TourAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'location',
        'description',
        'price',
    )


admin.site.register(OnlineCourse, OnlineCourseAdmin)
admin.site.register(Tour, TourAdmin)