from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

genders = (
    ('M', 'Мужской'),
    ('F', 'Женский'),
)

User = settings.AUTH_USER_MODEL

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30, choices=genders)
    birthday = models.CharField(max_length=10)
    pass_series = models.CharField(max_length=5)
    pass_number = models.CharField(max_length=10)
    inn = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)


class Role(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30, blank=True, null=True)

''' @receiver(post_save, sender=User)
def update_employee_signal(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance, role=)
    instance.employee.save() '''