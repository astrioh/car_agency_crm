from django.urls import path

from .views import *

urlpatterns = [
    path('', car_list_view),
    path('<int:car_id>', car_detailed_view)
]
