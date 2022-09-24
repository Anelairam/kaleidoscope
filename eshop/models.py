from django.db import models
from django.core.validators import FileExtensionValidator
from portfolio.models import Category, Type
from events.models import Difficulty

# Create your models here.
class Tutorial(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    difficulty = models.ForeignKey(Difficulty, null=True, on_delete=models.SET_NULL)
    file = models.FileField(null=True, validators=[FileExtensionValidator( ['mp4'] ) ])
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name
