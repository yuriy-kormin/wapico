from django.db import models

# Create your models here.
class Whatsapp(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, null=True)
    url = models.CharField(max_length=300, null=False)
