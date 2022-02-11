from django.contrib import admin

# Register your models here.
from .models import Workspace, Background

admin.site.register(Workspace)
admin.site.register(Background)
