from django.db import models


class DealerType(models.Model):
    name = models.CharField(max_length=30)


class Dealer(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(max_length=80, blank=True, null=True)
    contact = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=130, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30, blank=True, null=True)
    dealer_type = models.ForeignKey(DealerType, on_delete=models.CASCADE)