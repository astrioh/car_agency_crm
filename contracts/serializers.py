from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Contract, PaymentType
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from clients.models import Client
from clients.serializers import ClientSerializer
from cars.models import Car
from cars.serializers import CarSerializer


class ContractSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)
    client = ClientSerializer(read_only=True)
    car = CarSerializer(read_only=True)
    payment_type_name = serializers.CharField(source='payment_type.name', read_only=True)

    class Meta:
        model = Contract
        fields = ['id', 'employee', 'client', 'car', 'date', 'payment_type', 'payment_type_name', 'price']

    def create(self, validated_data):
        employee = get_object_or_404(Employee.objects.all(), pk=self.context.get('employee_id'))
        car = get_object_or_404(Car.objects.all(), pk=self.context.get('car_id'))
        payment_type = get_object_or_404(PaymentType.objects.all(), pk=self.context.get('payment_type_id'))
        client = get_object_or_404(Client.objects.all(), pk=self.context.get('client_id'))

        contract = Contract.objects.create(price=validated_data.get('price'), 
            car=car, 
            employee=employee, 
            payment_type=payment_type, 
            client=client)

        return contract



class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ['id', 'name']