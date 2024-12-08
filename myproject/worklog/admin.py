from django.contrib import admin

# Register your models here.
from .models import TypeOfWork, Worklog
admin.site.register(TypeOfWork)
admin.site.register(Worklog)
