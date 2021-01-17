from rest_framework import serializers

from .models import Car, Defect, CarPhoto


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ['id', 'image']


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



