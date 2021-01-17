from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from ..serializers import CarFullInfoSerializer, CarDefaultSerializer
from ..models import Car


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def car_list_view(request, *args, **kwargs):
    qs = Car.objects.all().order_by('-id')

    paginator = PageNumberPagination()
    paginator.page_size = 10

    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = CarFullInfoSerializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def car_detailed_view(request, car_id, *args, **kwargs):
    qs = Car.objects.filter(id=car_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    serializer = CarFullInfoSerializer(obj)

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
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def car_create_view(request, *args, **kwargs):
    serializer = CarDefaultSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({"message": "Failed to create a car"}, status=400)


@api_view(['POST'])
def car_delete_view(request, car_id, *args, **kwargs):
    qs = Car.objects.filter(id=car_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    obj.delete()

    return Response({"message": "Tweet deleted successfully"}, status=200)


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def car_edit_view(request, car_id, *args, **kwargs):
    qs = Car.objects.filter(id=car_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()

    serializer = CarDefaultSerializer(obj, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=202)

    return Response({"message": "Failed to edit a car"}, status=400)