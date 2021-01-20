from rest_framework import serializers

from .models import (
    Car, 
    Defect, 
    CarPhoto, 
    CarModel, 
    CarType, 
    EngineType, 
    BodyType, 
    Brand, 
    DefectType, 
    DrivetrainType, 
    TransmissionType
)


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['id', 'image', 'car']


class DefectSerializer(serializers.ModelSerializer):
    defect_type_name = serializers.CharField(source='defect_type.name', read_only=True)

    class Meta:
        model = Defect
        fields = ['defect_type', 'defect_type_name', 'name', 'text', 'image']


class CarSerializer(serializers.ModelSerializer):
    car_model_name = serializers.CharField(source='car_model.name', read_only=True)
    brand_name = serializers.CharField(source='car_model.brand.name', read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    car_type_name = serializers.CharField(source='car_type.name', read_only=True)
    body_type_name = serializers.CharField(source='body_type.name', read_only=True)
    drivetrain_type_name = serializers.CharField(source='drivetrain_type.name', read_only=True)
    transmission_type_name = serializers.CharField(source='transmission_type.name', read_only=True)
    engine_type_name = serializers.CharField(source='engine_type.name', read_only=True)
    car_photos = CarPhotoSerializer(source='get_photos', many=True)
    defects = DefectSerializer(source='get_defects', many=True)

    class Meta:
        model = Car
        fields = ['id', 'brand_name', 'car_model', 'car_model_name', 'dealer', 'dealer_name', 'pts', 'vin', 
            'car_type', 'car_type_name', 'release_year', 'price', 'color', 'mileage', 'wheel', 'drivetrain_type', 
            'drivetrain_type_name', 'body_type', 'body_type_name', 'transmission_type', 'transmission_type_name', 
            'engine_type', 'engine_type_name', 'engine_volume', 'engine_power', 'car_photos', 'defects', 'active']


# Car misc serializers. They all use same view where they are schosen by "switch" statement
class DefectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefectType
        fields = ['id', 'name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

class CarModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'brand', 'brand_name']

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ['id', 'name']

class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = ['id', 'name']

class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = ['id', 'name']

class DrivetrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrivetrainType
        fields = ['id', 'name']

class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionType
        fields = ['id', 'name']