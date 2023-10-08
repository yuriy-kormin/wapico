from celery.result import AsyncResult
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from .forms import SendForm
from django.contrib import messages
from wapico.tasks import process_task
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
            # 'task_results': TaskResult.objects.all()
            'task_results': TaskResult.objects.filter(task_name='task').
            values_list(
                'id',
                'task_id',
                'status',
                'date_created'
            )
        })
        return context

    def form_valid(self, form):
        result = process_task.delay(
            form.cleaned_data['time1'],
            form.cleaned_data['time2'],
        )
        messages.info(
            self.request, result.get()
        )
        return super().form_valid(form)


class TaskResultView(DetailView):
    model = TaskResult
    template_name = "task/task_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj_id = self.kwargs.get('pk')
        obj = TaskResult.objects.get(pk=obj_id)
        taskid = obj.task_id
        result = AsyncResult(taskid)
        # result.save()
        context.update({
            'res': [
                {
                    'info': res.kwargs,
                    'status': res.status,
                    'date': res.date_done,
                    'response': res.info,
                } for res in result.children[0] if len(result.children)],
        })
        return context
