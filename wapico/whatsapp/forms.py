from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Whatsapp


class InstanceForm(forms.ModelForm):
    class Meta:
        model = Whatsapp
        fields = [
            'name',
            'instance',
            'phone_number',
            'token',
        ]
