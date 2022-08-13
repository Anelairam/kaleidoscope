from django.contrib import admin
from .models import Photo, Category, OnlineCourse, Tour
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'label',
        'price',
        'sku',
        'size',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


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


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(OnlineCourse, OnlineCourseAdmin)
admin.site.register(Tour, TourAdmin)