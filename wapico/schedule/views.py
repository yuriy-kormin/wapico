from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from .models import Schedule
from .forms import ScheduleForm
from django_celery_beat.models import CrontabSchedule


# Create your views here.
class ScheduleCreateView(CreateView):
    form_class = ScheduleForm
    template_name = 'schedule/create.html'
    success_url = reverse_lazy("schedule_list")
    extra_context = {
        "button_title": "Create",
        "header": "Create schedule",
    }


class ScheduleUpdateView(UpdateView):
    model = CrontabSchedule
    form_class = ScheduleForm
    template_name = 'schedule/create.html'
    success_url = reverse_lazy("schedule_list")
    extra_context = {
        "button_title": "Update",
        "header": "Update schedule",
    }


class ScheduleListView(ListView):
    model = CrontabSchedule
    template_name = 'schedule/list.html'
