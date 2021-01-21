from django.contrib import admin

from .models import Employee, Role


admin.site.register([Employee, Role])