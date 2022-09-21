from django.contrib import admin
from .models import Product, Category, Type, Tutorial
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'location',
        'size',
        'description',
        'price',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'description',
        'price',
    )



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Tutorial, TutorialAdmin)
