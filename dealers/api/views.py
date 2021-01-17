from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import DealerSerializer
from ..models import Dealer


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def dealer_list_view(request, *args, **kwargs):
    response = list_view(Dealer, DealerSerializer, request, 20)
    return response


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
def dealer_create_view(request, *args, **kwargs):
    response = create_view(DealerSerializer, request, "Failed to add a new dealer")
    return response


@api_view(['POST'])
def dealer_delete_view(request, dealer_id, *args, **kwargs):
    response = delete_view(Dealer, dealer_id, "Dealer deleted successfully")


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def dealer_edit_view(request, dealer_id, *args, **kwargs):
    response = edit_view(Dealer, DealerSerializer, request, dealer_id, "Failed to edit a dealer")
    return response