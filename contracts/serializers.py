from rest_framework import serializers

from .models import Contract, PaymentType
from employees.serializers import EmployeeSerializer
from clients.serializers import ClientSerializer
from cars.serializers import CarSerializer


class ContractSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    payment_type_name = serializers.CharField(source='payment_type.name', read_only=True)

    class Meta:
        model = Contract
        fields = ['id', 'employee', 'client', 'car', 'date', 'payment_type', 'payment_type_name', 'price']


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ['id', 'name']