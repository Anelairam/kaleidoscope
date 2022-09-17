from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('Type', null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=25, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name