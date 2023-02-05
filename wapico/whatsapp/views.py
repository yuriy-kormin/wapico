from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import InstanceForm
from .models import Whatsapp


# Create your views here.
class WhatsappCreateView(CreateView, SuccessMessageMixin):
    form_class = InstanceForm
    template_name = 'whatsapp/create.html'
    success_url = reverse_lazy('instance_list')
    success_message = 'Instance created successfully'
    extra_context = {
        "button_title": 'Create'
    }


class WhatsappListView(ListView):
    model = Whatsapp
    template_name = 'whatsapp/list.html'
    queryset = Whatsapp.objects.all().order_by('id')


class WhatsappUpdateView(UpdateView, SuccessMessageMixin):
    form_class = InstanceForm
    model = Whatsapp
    template_name = 'whatsapp/create.html'
    success_url = reverse_lazy('instance_list')
    success_message = 'Instance updated successfully'
    extra_context = {
        "button_title": 'Update'
    }
