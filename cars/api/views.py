from django.db.models import Q 
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view

from ..serializers import (
    CarSerializer, 
    DefectSerializer, 
    CarPhotoSerializer, 
    CarModelSerializer, 
    CarTypeSerializer, 
    EngineTypeSerializer, 
    BodyTypeSerializer, 
    BrandSerializer, 
    DefectTypeSerializer, 
    DrivetrainTypeSerializer, 
    TransmissionTypeSerializer
)

from ..models import (
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


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def car_list_view(request, *args, **kwargs):
    search_str = request.GET.get('search') or ''

    qs = Car.objects.filter(Q(car_model__name__icontains=search_str) | Q(car_model__brand__name__icontains=search_str)).order_by('-id')

    paginator = PageNumberPagination()
    paginator.page_size = 20

    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = CarSerializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def car_detailed_view(request, car_id, *args, **kwargs):
    qs = Car.objects.filter(id=car_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    serializer = CarSerializer(obj)

    return Response(serializer.data, status=200)


'''
{
    "car_model": 1, 
    "dealer": 1, 
    "pts": "321", 
    "vin": "312", 
    "car_type": 1, 
    "release_year": 222, 
    "price": "31321",
    "color": "bas", 
    "mileage": 3123, 
    "wheel": "fdsf",
    "body_type": 1, 
    "drivetrain_type": 1,
    "transmission_type": 1, 
    "engine_type": 1, 
    "engine_volume": "23.2", 
    "engine_power": 412, 
    "active": true
}

TODO: handle multiple images and multiple defects upload
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def car_create_view(request, *args, **kwargs):
    response = create_view(CarSerializer, request, "Failed to create a car")
    return response


@api_view(['POST'])
def car_delete_view(request, car_id, *args, **kwargs):
    response = delete_view(Car, car_id, "Car deleted successfully")
    return response


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def car_edit_view(request, car_id, *args, **kwargs):
    response = edit_view(Car, CarSerializer, request, car_id, "Failed to edit a car")
    return response


misc_models = {
    'defect_type': DefectType,
    'brand': Brand,
    'car_model': CarModel,
    'car_type': CarType,
    'engine_type': EngineType,
    'body_type': BodyType,
    'drivetrain_type': DrivetrainType,
    'transmission_type': TransmissionType,
}

misc_serializers = {
    'defect_type': DefectTypeSerializer,
    'brand': BrandSerializer,
    'car_model': CarModelSerializer,
    'car_type': CarTypeSerializer,
    'engine_type': EngineTypeSerializer,
    'body_type': BodyTypeSerializer,
    'drivetrain_type': DrivetrainTypeSerializer,
    'transmission_type': TransmissionTypeSerializer,
}
'''
{
    "model": "car_type",
    "name": "New Car Type"
}
'''
@api_view(['POST'])
def misc_create_view(request, model_name, *args, **kwargs):

    if model_name in misc_serializers:
        return create_view(misc_serializers[model_name], request)
    
    return Response({"message": "There is no model like that"}, 404)


@api_view(['POST'])
def misc_delete_view(request, model_name, id_model, *args, **kwargs):
    if model_name in misc_models:
        return delete_view(misc_models[model_name], id_model)
    
    return Response({"message": "There is no model like that"}, 404)


@api_view(['POST'])
def misc_edit_view(request, model_name, id_model, *args, **kwargs):
    if model_name in misc_models and model_name in misc_serializers:
        return edit_view(misc_models[model_name], misc_serializers[model_name], request, id_model)
    
    return Response({"message": "There is no model like that"}, 404)