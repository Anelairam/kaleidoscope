from portfolio.models import Category, Type
from django.db import models


# Create your models here.
class Difficulty(models.Model):
    class Meta:
        verbose_name_plural = 'Difficulty'

    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.difficulty


class Event(models.Model):
    title = models.CharField(max_length=25)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    day = models.DateField()
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    difficulty = models.ForeignKey('Difficulty', null=True, on_delete=models.SET_NULL)
    starting_at = models.TimeField()
    ending_at = models.TimeField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


