from rest_framework import serializers
import json

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
    car_photos = CarPhotoSerializer(source='get_photos', many=True, required=False)
    defects = DefectSerializer(source='get_defects', many=True, required=False)

    def create(self, validated_data):
        images = self.context.get('request').POST.getlist('car_photos[]')
        defects = self.context.get('request').POST.getlist('defects[]')

        print(defects)
        for val in validated_data:
            print(validated_data[val])

        car = Car.objects.create(
            car_model=validated_data.get('car_model'),
            car_type=validated_data.get('car_type'),
            dealer=validated_data.get('dealer'),
            pts=validated_data.get('pts'),
            vin=validated_data.get('vin'),
            color=validated_data.get('color'),
            mileage=validated_data.get('mileage'),
            release_year=validated_data.get('release_year'),
            price=validated_data.get('price'),
            engine_type=validated_data.get('engine_type'),
            engine_volume=validated_data.get('engine_volume'),
            engine_power=validated_data.get('engine_power'),
            body_type=validated_data.get('body_type'),
            drivetrain_type=validated_data.get('drivetrain_type'),
            transmission_type=validated_data.get('transmission_type')
        )

        for image in images:
            CarPhotoSerializer.create(CarPhotoSerializer(), validated_data={'car': car, 'image': image})


        for defect in defects:
            defect = json.loads(defect)
            print(defect)
            defect_type = DefectType.objects.get(id=defect['defect_type'])
            defect_data = {
                'car': car, 
                'defect_type': defect_type,
                'name': defect['name'],
                'text': defect['text'],
                'image': defect['image']
            }
            DefectSerializer.create(DefectSerializer(), validated_data=defect_data)

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