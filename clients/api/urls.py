from django.urls import path

from .views import *

urlpatterns = [
    path('', client_list_view),
    path('create/', client_create_view),
    path('<int:client_id>/delete', client_delete_view),
    path('<int:client_id>/edit', client_edit_view),
]