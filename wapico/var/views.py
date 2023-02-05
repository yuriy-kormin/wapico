from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import \
    ListView, CreateView, UpdateView, DeleteView

from .models import Var


# Create your views here.
class VarListView(ListView):
    model = Var
    template_name = 'var/list.html'
    queryset = Var.objects.all().order_by('id')


class VarUpdateView(UpdateView):
    model = Var
    fields = '__all__'
    template_name = 'var/create.html'
    success_url = reverse_lazy('var_list')
    extra_context = {
        "button_title": 'Update'
    }


class VarCreateView(CreateView):
    model = Var
    fields = '__all__'
    template_name = 'var/create.html'
    success_url = reverse_lazy('var_list')
    extra_context = {
        "button_title": 'Create'
    }