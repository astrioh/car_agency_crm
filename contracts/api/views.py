from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import ContractSerializer, PaymentTypeSerializer
from ..models import Contract, PaymentType


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def contract_list_view(request, *args, **kwargs):
    response = list_view(Contract, ContractSerializer, request, 20)
    return response


'''
{
}
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def contract_create_view(request, *args, **kwargs):
    response = create_view(ContractSerializer, request, "Failed to add a new contract")
    return response


@api_view(['POST'])
def contract_delete_view(request, contract_id, *args, **kwargs):
    response = delete_view(Contract, contract_id, "contract deleted successfully")


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def contract_edit_view(request, contract_id, *args, **kwargs):
    response = edit_view(Contract, ContractSerializer, request, contract_id, "Failed to edit a contract")
    return response