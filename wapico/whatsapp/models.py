from django.db import models


# Create your models here.
class Whatsapp(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, null=True)
    instance = models.CharField(max_length=30, null=False, default="")
    phone_number = models.CharField(max_length=30, null=False, default="")
    token = models.CharField(max_length=50, null=False, default="")
