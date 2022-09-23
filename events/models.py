from django.db import models
import calendar

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=25)
    day = models.DateField()
    starting_at = models.TimeField()
    ending_at = models.TimeField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Calendar(calendar.HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        
    
    def formatday(self, day, events):
        daily_events = events.filter(starting_at__day=day)
        d = ''
        for event in daily_events:
            d += f'<li> {event.title} </li>'

        if day != 0:
            return f"<td><span class='day'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        w = ''
        for d, weekday in theweek:
            w += self.formatday(d, events)
        return f'<tr> {w} </tr>'

    def formatmonth(self, withyear=True):
        events = Event.objects.filter(starting_at__year=self.year, starting_at__month=self.month)

        cd = f'<table class="cal">\n'
        cd += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}/n'
        cd += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cd += f'{self.formatweek(w, events)}\n'
        return cd
        