from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from ..serializers import CarSerializer
from ..models import Car


@api_view(['GET'])
def car_list_view(request, *args, **kwargs):
    qs = Car.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 10

    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = CarSerializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)

def car_detailed_view(request, car_id, *args, **kwargs):
    qs = Car.objects.filter(id=car_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    serializer = CarSerializer(obj)

    return Response(serializer.data, status=200)