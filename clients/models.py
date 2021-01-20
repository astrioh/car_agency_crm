from django.db import models


class Client(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20)
    birthday = models.DateField()
    pass_series = models.CharField(max_length=5)
    pass_number = models.CharField(max_length=10)
    address = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)