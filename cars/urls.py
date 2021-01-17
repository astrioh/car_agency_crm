from django.urls import path, include

from .views import *

urlpatterns = [
    path('', car_all_view),
    path('<int:car_id>', car_detailed_view)
]