from django.contrib import admin
<<<<<<< HEAD
from .models import Product, Category, Type, Tutorial
=======
from .models import Product, Category, Type
>>>>>>> parent of aaf93d4 (Create Tutorial dna tour models)
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

<<<<<<< HEAD
class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'type',
        'description',
        'price',
    )

=======
>>>>>>> parent of aaf93d4 (Create Tutorial dna tour models)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
<<<<<<< HEAD
admin.site.register(Type, TypeAdmin)
admin.site.register(Tutorial, TutorialAdmin)
=======
admin.site.register(Type, TypeAdmin)
>>>>>>> parent of aaf93d4 (Create Tutorial dna tour models)
