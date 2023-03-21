from django.db import models
from django_celery_beat.models import CrontabSchedule, PeriodicTask


class Schedule(models.Model):
    crontab_schedule = models.ForeignKey(CrontabSchedule,
                                         on_delete=models.CASCADE)
