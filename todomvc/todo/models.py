from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)
