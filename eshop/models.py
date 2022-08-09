from django.db import models
from portfolio.models import Category

# Create your models here.
class OnlineCourse(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    sku = models.CharField(max_length=100, null=True, blank=True)


class Tour(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)