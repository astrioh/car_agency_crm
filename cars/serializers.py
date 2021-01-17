from rest_framework import serializers

from .models import Car

class CarFullInfoSerializer(serializers.ModelSerializer):
    car_model_name = serializers.CharField(source='car_model.name', read_only=True)
    brand_name = serializers.CharField(source='car_model.brand.name', read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    car_type_name = serializers.CharField(source='car_type.name', read_only=True)
    body_type_name = serializers.CharField(source='body_type.name', read_only=True)
    drivetrain_type_name = serializers.CharField(source='drivetrain_type.name', read_only=True)
    transmission_type_name = serializers.CharField(source='transmission_type.name', read_only=True)
    engine_type_name = serializers.CharField(source='engine_type.name', read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand_name', 'car_model_name', 'dealer_name', 'pts', 'vin', 
            'car_type_name', 'release_year', 'price', 'color', 'mileage', 'wheel', 'drivetrain_type_name',
            'body_type_name', 'transmission_type_name', 'engine_type_name', 'engine_volume', 'engine_power', 
            'active']


class CarDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_model', 'dealer', 'pts', 'vin', 
            'car_type', 'release_year', 'price', 'color', 'mileage', 'wheel', 'drivetrain_type',
            'body_type', 'transmission_type', 'engine_type', 'engine_volume', 'engine_power', 
            'active']
