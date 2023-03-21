from django import forms
from django_celery_beat.models import CrontabSchedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = CrontabSchedule
        fields = (
        'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year')

    minute_2 = forms.CharField(label='Minute2', max_length=2)
    # hour = forms.CharField(label='Hour', max_length=2)
    # day_of_month = forms.CharField(label='Day of Month', max_length=2)
    # month_of_year = forms.CharField(label='Month of Year', max_length=2)
    # day_of_week = forms.CharField(label='Day of Week', max_length=1)
