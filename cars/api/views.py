from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import CarSerializer
from ..models import Car


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def car_list_view(request, *args, **kwargs):
    response = list_view(Car, CarSerializer, request, 10)
    return response


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
"name": "dealer name",
"contact": "dealer contact",
"address": "dealer address",
"phone": "dealer phone",
"email": "dealer email",
"dealer_type": 1
}
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