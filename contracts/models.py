from django.db import models

from clients.models import Client
from cars.models import Car
from employees.models import Employee


class Contract(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=18, decimal_places=0)
    payment_type = models.ForeignKey('PaymentType', on_delete=models.CASCADE)


class PaymentType(models.Model):
    name = models.CharField(max_length=30)