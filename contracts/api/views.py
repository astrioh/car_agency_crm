from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employees.models import Employee
from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import ContractSerializer, PaymentTypeSerializer
from ..models import Contract, PaymentType


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def contract_list_view(request, *args, **kwargs):
    response = list_view(Contract, ContractSerializer, request, 20)
    return response



@api_view(['GET'])
def payment_list_view(request, *args, **kwargs):
    response = list_view(PaymentType, PaymentTypeSerializer, request, 100)
    return response
'''
{
}
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def contract_create_view(request, *args, **kwargs):
    user_role = Employee.objects.get(user=request.user).role.name
    if user_role != 'consultant':
        return Response({"message": "У вас нет доступа к заключению контрактов"}, status=403)
    
    serializer = ContractSerializer(data=request.data, 
        context={
            'employee_id': int(request.data.get('employee')), 
            'client_id': int(request.data.get('client')), 
            'car_id': int(request.data.get('car')), 
            'payment_type_id': int(request.data.get('payment_type'))})

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({"message": error_message}, status=400)


@api_view(['POST'])
def contract_delete_view(request, contract_id, *args, **kwargs):
    response = delete_view(Contract, contract_id, "contract deleted successfully")


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def contract_edit_view(request, contract_id, *args, **kwargs):
    response = edit_view(Contract, ContractSerializer, request, contract_id, "Failed to edit a contract")
    return response