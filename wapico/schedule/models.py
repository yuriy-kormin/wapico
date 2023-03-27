# from django.db import models
# from django_celery_beat.models import PeriodicTask
#
#
#
from django.db import models
from django_celery_beat.models import PeriodicTask, CrontabSchedule


# class Schedule(models.Model):
    # crontab_schedule = models.ForeignKey(CrontabSchedule,
    #                                      on_delete=models.CASCADE)

# from django.db import models
# from django_celery_beat.models import PeriodicTask
#
#
# #
# from django.db import models
# from django_celery_beat.models import PeriodicTask, CrontabSchedule
#
#
# class Schedule(CrontabSchedule):
#     task = models.ForeignKey(PeriodicTask, on_delete=models.CASCADE)
#     time_from = models.IntegerField(
#         help_text='Set time period start (in seconds)'
#     )
#     time_from = models.IntegerField(
#         help_text='Set time period end (in seconds)'
#     )
