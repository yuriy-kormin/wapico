from django.db import models


# Create your models here.
class Var(models.Model):
    GLOBAL_VARS = ['base_url', 'format']
    # This vars must be set and cannot be deleted
    GENERATED_VARS = ['phone_number', 'message']
    # This vars must be replaced by values in task function(tasks.py)
    name = models.CharField(max_length=30, null=False, unique=True)
    value = models.CharField(max_length=300, null=True)
    FAKER_TEXT_LEN = 30

    def __str__(self):
        return self.name
    @classmethod
    def get_value(cls, name):
        return cls.objects.get(name=name).value
    @classmethod
    def get_global_vars(cls):
        return cls.objects.values_list('name', flat=True)
