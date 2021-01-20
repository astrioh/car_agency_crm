from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import ClientSerializer
from ..models import Client


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def client_list_view(request, *args, **kwargs):
    response = list_view(Client, ClientSerializer, request, 20)
    return response


'''
{
    "first_name": "first_name",
    "last_name": "last_name",
    "middle_name": "middle_name",
    "phone": "+12312321",
    "birthday": "2000-09-21",
    "pass_series": "1234",
    "pass_number": "123456",
    "email": "email@email.com",
    "address": "address"
}
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def client_create_view(request, *args, **kwargs):
    response = create_view(ClientSerializer, request, "Failed to add a new client")
    return response


@api_view(['POST'])
def client_delete_view(request, client_id, *args, **kwargs):
    response = delete_view(Client, client_id, "Dealer deleted successfully")


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def client_edit_view(request, client_id, *args, **kwargs):
    response = edit_view(Client, ClientSerializer, request, client_id, "Failed to edit a client")
    return response