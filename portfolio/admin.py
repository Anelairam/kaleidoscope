from django.contrib import admin
from .models import Photo, Category
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


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Category, CategoryAdmin)