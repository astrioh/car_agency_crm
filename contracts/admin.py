from django.contrib import admin

from .models import Contract, PaymentType

admin.site.register([Contract, PaymentType])