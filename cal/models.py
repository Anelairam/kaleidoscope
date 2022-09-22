from django.db import models


# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	day = models.DateField()
	starting_at = models.TimeField()
	ending_at = models.TimeField()
	event_description = models.CharField(max_length=500)

	def __str__(self):
		return self.title
