from django.conf import settings
from django.db import models

# Create your models here.

class Period(models.Model):
    per_type = models.IntegerField()
    per_interval = models.IntegerField()
    per_week_occurences = models.IntegerField()
    per_end_date = models.DateField()
    per_num_of_repeats = models.IntegerField()

class Event(models.Model):
    evt_name = models.CharField(max_length=45)
    evt_place = models.CharField(max_length=45)
    evt_start_time = models.TimeField()
    evt_end_time = models.TimeField()
    evt_date = models.DateField()
    evt_note = models.TextField()
    per = models.ForeignKey(Period)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

class Alarm(models.Model):
    alm_time = models.BigIntegerField()
    alm_type = models.IntegerField()
    evt = models.ForeignKey(Event)

class Exception(models.Model):
    evt = models.ForeignKey(Event)
    ex_date = models.DateField()
