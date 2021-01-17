from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register([Car, CarModel, CarType, CarPhoto, EngineType, BodyType, Brand, DefectType, Defect, DrivetrainType, TransmissionType])