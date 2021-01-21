"""
car_agency_crm URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('api/cars/', include('cars.api.urls')),
    path('api/dealers/', include('dealers.api.urls')),
    path('api/clients/', include('clients.api.urls')),
    path('api/employees/', include('employees.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)