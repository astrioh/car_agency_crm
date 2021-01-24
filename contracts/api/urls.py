from django.urls import path

from .views import *

urlpatterns = [
    path('', contract_list_view),
    path('payment_types/', payment_list_view),
    path('create/', contract_create_view),
    path('<int:contract_id>/delete', contract_delete_view),
    path('<int:contract_id>/edit', contract_edit_view),
]
