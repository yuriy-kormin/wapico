import re
from wapico.var.models import Var
from django.db import models


# Create your models here.
class Whatsapp(models.Model):
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True)
    instance = models.CharField(max_length=30, null=False, default="")
    phone_number = models.CharField(max_length=30, null=False, default="")
    token = models.CharField(max_length=50, null=False, default="")
    group = models.PositiveSmallIntegerField(default=1, null=False)

    def get_url(self):
        url = Var.objects.get(name='format').value
        format_vars = set(re.findall("{{\w*}}", url))
        for var in format_vars:
            var_name = var[2:-2]
            if var_name in Var.get_global_vars():
                url = re.sub(var, Var.get_value(var_name), url)
            elif var_name in self.get_fields_names():
                url = re.sub(var, getattr(self, var_name), url)
            else:
                ValueError('error in global "format" setting')
        return url

    def get_fields_names(self):
        return [field.name for field in self.__class__._meta.get_fields()]
