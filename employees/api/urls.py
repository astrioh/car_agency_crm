from django.urls import path

from .views import *

urlpatterns = [
    path('', employee_list_view),
    path('create/', employee_create_view),
    path('<int:employee_id>/delete', employee_delete_view),
    path('<int:employee_id>/edit', employee_edit_view),
    path('get_auth_employee', employee_logged_view),
]
