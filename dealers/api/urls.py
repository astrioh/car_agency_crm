from django.urls import path

from .views import *

urlpatterns = [
    path('', dealer_list_view),
    path('create/', dealer_create_view),
    path('<int:dealer_id>/delete', dealer_delete_view),
    path('<int:dealer_id>/edit', dealer_edit_view),
]
