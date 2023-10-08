import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import PeriodicTaskForm, CrontabForm
from django_celery_beat.models import CrontabSchedule, PeriodicTask

class ScheduleCreateView(CreateView):
    model = CrontabSchedule
    form_class = CrontabForm
    success_url = reverse_lazy('schedule_list')
    template_name = 'schedule/create.html'
    extra_context = {
        "button_title": "Create",
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     if self.request.POST:
    #         context['schedule'] = CrontabScheduleFormSet(
    #             self.request.POST)
    #         logging.error(context)
    #     else:
    #         context['schedule'] = CrontabScheduleFormSet()
    #     return context
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     crontab_formset = context['schedule']
    #     if crontab_formset.is_valid() and form.is_valid():
    #         self.object = form.save()
    #         crontabs = crontab_formset.save(commit=False)
    #         for crontab in crontabs:
    #             crontab.task = self.object
    #             crontab.save()
    #     return super().form_valid(form, crontab_formset)


class ScheduleUpdateView(UpdateView):
    # pass
    model = CrontabSchedule
    success_url = reverse_lazy("schedule_list")
    form_class = CrontabForm
    template_name = 'schedule/create.html'
    # success_url = reverse_lazy("schedule_list")
    extra_context = {
        "button_title": "Update",
        "button_delete": "Delete",
        #     "header": "Update schedule",
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['schedule'] = CustomPeriodicTaskFormSet(
    #         instance=self.object.crontab
    #     )
    #     return context

    # def form_valid(self, form):
    #     # return super().form_valid(form)
    #
    #     raise IOError(form)
    #     context = self.get_context_data()
    #     schedule_form = context['schedule_form']
    #     self.object = form.save()
    #     schedule_form.instance = self.object.schedule
    #     schedule_form = CrontabForm(self.request.POST,
    #                                          instance=schedule_form.instance)
    #     if relatedmodel_form.is_valid():
    #         relatedmodel_form.save()
    #     # return super().form_valid(form)


class ScheduleListView(ListView):
    model = CrontabSchedule
    template_name = 'schedule/list.html'
    queryset = CrontabSchedule.objects.exclude(
        periodictask__task='celery.backend_cleanup')


class ScheduleDeleteView(DeleteView):
    model = CrontabSchedule
    template_name = 'schedule/delete.html'
    success_url = reverse_lazy('schedule_list')
    extra_context = {
        "button_delete": "Delete",
    }


class PeriodicTaskCreateView(CreateView):
    model = PeriodicTask
    form_class = PeriodicTaskForm
    template_name = "schedule/pt/create.html"
    success_url = reverse_lazy('pt_list')
    extra_context = {
        "button_title": "Create",
    }

    def form_valid(self, form):
        form.instance.task = 'task'
        return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.form:
    #         PeriodicTaskForm(self.request.POST)
    #     return context

class PeriodicTaskUpdateView(UpdateView):
    model = PeriodicTask
    form_class = PeriodicTaskForm
    success_url = reverse_lazy("pt_list")
    template_name = 'schedule/pt/create.html'
    extra_context = {
        "button_title": "Update",
        "button_delete": "Delete",
    }
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.form:
    #         PeriodicTaskForm(self.request.POST)
    #     return context


class PeriodicTaskDeleteView(DeleteView):
    model = PeriodicTask
    template_name = 'schedule/pt/delete.html'
    success_url = reverse_lazy('pt_list')
    extra_context = {
        "button_delete": "Delete",
    }


class PeriodicTaskListView(ListView):
    model = PeriodicTask
    template_name = "schedule/pt/list.html"
    queryset = PeriodicTask.objects.filter(task='task')
