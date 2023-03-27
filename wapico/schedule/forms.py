from django import forms
from django.forms import inlineformset_factory
from django_celery_beat.models import PeriodicTask, CrontabSchedule


# from .models import Schedule

class CrontabForm(forms.ModelForm):
    class Meta:
        model = CrontabSchedule
        # fields = 'minute', 'hour', 'day_of_month', 'day_of_week', 'month_of_year'
        # fields = '__all__'
        exclude = 'timezone',


class PeriodicTaskForm(forms.ModelForm):
    # time_from = forms.IntegerField(min_value=0)
    # time_to = forms.IntegerField(min_value=0)

    # def __init__(self,*args,**kwargs):
    #     super(PeriodicTaskForm, self).__init__(*args, **kwargs)
    #     if
    #     self.time_from
    class Meta:
        model = PeriodicTask
        fields = 'name', 'crontab', 'enabled', 'args'


# CrontabScheduleFormSet = inlineformset_factory(
#     PeriodicTask,
#     Schedule,
#     form=CrontabForm,
#     extra=1,
#     can_delete=False,
# )

# from django.forms import ModelForm, inlineformset_factory
# from django_celery_beat.models import CrontabSchedule, PeriodicTask
#
#
# # from .models import CustomPeriodicTask
#
#
# class PeriodicTaskForm(ModelForm):
#     class Meta:
#         model = PeriodicTask
#         fields = ['name', 'task', 'enabled']
#
#
# ScheduleFormSet = inlineformset_factory(
#         PeriodicTask,
#         CrontabSchedule,
#         fields=['minute', 'hour', 'day_of_week', 'day_of_month',
#                 'month_of_year'],
#         extra=1,
#         can_delete=True
#     )
#
# # from django import forms
# # from django_celery_beat.models import PeriodicTask
# #
# # from django import forms
# # from django.forms import inlineformset_factory
# # from django_celery_beat.models import CrontabSchedule, PeriodicTask
# #
# #
# # class CrontabScheduleForm(forms.ModelForm):
# #     class Meta:
# #         model = CrontabSchedule
# #         fields = (
# #             'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'
# #         )
# #
# #
# # class ScheduleForm(forms.ModelForm):
# #     crontab = inlineformset_factory(PeriodicTask, CrontabSchedule,
# #                                     fields=('minute', 'hour')
# #                                     )
# #
# #     # form=CrontabScheduleForm, can_delete=False)
# #
# #     class Meta:
# #         model = PeriodicTask
# #         fields = ('name', 'args', 'enabled')
# #
# # # class ScheduleForm(forms.ModelForm):
# # #     class Meta:
# # #         model = PeriodicTask
# # #         fields = [
# # #             'name', 'enabled', 'crontab__minute', 'args'
# # #         ]
# # # from django_celery_beat.models import CrontabSchedule
# # #
# # #
# # # class ScheduleForm(forms.ModelForm):
# # #     name = forms.CharField(
# # #         help_text='Set task name',
# # #         max_length=50,
# # #         required=True,
# # #     )
# # #     time_from = forms.IntegerField(
# # #         help_text='Set time period start (in seconds)',
# # #         required=True,
# # #     )
# # #     time_to = forms.CharField(
# # #         help_text='Set time period end (in seconds)',
# # #         required=True,
# # #     )
# # #     active = forms.BooleanField(initial=True)
# # #
# # #     class Meta:
# # #         model = CrontabSchedule
# # #         fields = (
# # #             'minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'
# # #         )
