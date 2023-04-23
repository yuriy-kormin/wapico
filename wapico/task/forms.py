import requests

from django import forms
from wapico.whatsapp.models import Whatsapp
from celery import shared_task


class SendForm(forms.Form):
    # tt = forms.CharField(label='test')
    time1 = forms.IntegerField(label='from')
    time2 = forms.IntegerField(label='to')
