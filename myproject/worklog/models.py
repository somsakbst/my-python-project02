from django.db import models
from django.utils.timezone import now

# Create your models here.
class Worklog(models.Model):
    timestamp = models.DateTimeField(default = now())
    typeOfWork = models.ForeignKey('TypeOfWork', on_delete=models.CASCADE)
    work_text = models.TextField(default="")
    manhour = models.FloatField(default=0)
    def __str__(self):
        return self.work_text

class TypeOfWork(models.Model):
    typeOfWork_text = models.CharField(max_length=200)
    def __str__(self):
        return self.typeOfWork_text
