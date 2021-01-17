from rest_framework import serializers

from .models import Car

class CarSerializer(serializers.ModelSerializer):
    car_model_name = serializers.RelatedField(source='car_model', read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'car_model_name', 'dealer', 'pts', 'vin', 'car_type']