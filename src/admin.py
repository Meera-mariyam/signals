from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Task)
admin.site.register(Taskdate)
admin.site.register(History)