from rest_framework import serializers

from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'phone', 'birthday',
            'pass_series', 'pass_number', 'address', 'email']