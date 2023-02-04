from django.db import models


# Create your models here.
class Var(models.Model):
    name = models.CharField(max_length=30, null=False)
    value = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name