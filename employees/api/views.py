from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from car_agency_crm.utils.standard_views import list_view, create_view, delete_view, edit_view
from ..serializers import EmployeeSerializer
from ..models import Employee


@api_view(['GET'])
#@authentication_classes([IsAuthenticated])
def employee_list_view(request, *args, **kwargs):
    response = list_view(Employee, EmployeeSerializer, request, 20)
    return response


'''
{
    "name": "employee name",
    "contact": "dealer contact",
    "address": "dealer address",
    "phone": "dealer phone",
    "email": "dealer email",
    "dealer_type": 1
}
'''
@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def employee_create_view(request, *args, **kwargs):
    response = create_view(EmployeeSerializer, request, "Failed to add a new employee")
    return response


@api_view(['POST'])
def employee_delete_view(request, employee_id, *args, **kwargs):
    response = delete_view(Employee, employee_id, "Dealer deleted successfully")


@api_view(['POST'])
#@authentication_classes([IsAuthenticated])
def employee_edit_view(request, employee_id, *args, **kwargs):
    response = edit_view(Employee, EmployeeSerializer, request, employee_id, "Failed to edit a employee")
    return response