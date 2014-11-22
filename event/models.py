from django.db import models

# Create your models here.

class Periods(models.Model):
    per_type = models.IntegerField()
    per_interval = models.IntegerField()
    per_week_occurences = models.IntegerField()
    per_end_date = models.DateField()
    per_num_of_repeats = models.IntegerField()

class Events(models.Model):
    evt_name = models.CharField(max_length=45)
    evt_place = models.CharField(max_length=45)
    evt_start_time = models.DateTimeField()
    evt_end_time = models.DateTimeField()
    evt_date = models.DateField()
    evt_note = models.TextField()
    per = models.ForeignKey(Periods)

class Alarms(models.Model):
    alm_time = models.BigIntegerField()
    alm_type = models.IntegerField()
    evt = models.ForeignKey(Events)

class Exceptions(models.Model):
    evt = models.ForeignKey(Events)
    ex_date = models.DateField()
