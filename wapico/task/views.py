from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from .forms import SendForm
from django.contrib import messages
from .tasks import make_result
from django_celery_results.models import TaskResult


class SendView(FormView):
    form_class = SendForm
    template_name = "task/send.html"
    success_url = reverse_lazy('root')
    extra_context = {
        'header': 'Task send',
        'header_list': "Task list",
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'task_results': TaskResult.objects.values_list(
                'id',
                'task_id',
                'status',
                'date_created'
            )
        })
        return context

    def form_valid(self, form):
        messages.info(
            self.request, make_result.delay(
                form.cleaned_data['time1'],
                form.cleaned_data['time2'],
            )
        )
        return super().form_valid(form)


class TaskResultView(DetailView):
    model = TaskResult
    template_name = "task/task_view.html"
