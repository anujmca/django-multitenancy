from django.db import models

# Create your models here.
from sweet_shared.models_shared import SweetType


class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name