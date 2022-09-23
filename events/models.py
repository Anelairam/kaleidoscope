from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=25)
    day = models.DateField()
    starting_at = models.TimeField()
    ending_at = models.TimeField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title