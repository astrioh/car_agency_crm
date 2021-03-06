from django.urls import path

from .views import *

urlpatterns = [
    path('', car_list_view),
    path('<int:car_id>', car_detailed_view),
    path('create/', car_create_view),
    path('<int:car_id>/delete', car_delete_view),
    path('<int:car_id>/edit', car_edit_view),
    path('misc/', misc_list_view),
    path('misc/<str:model_name>/create/', misc_create_view),
    path('misc/<str:model_name>/<int:id_model>/create/', misc_delete_view),
]
