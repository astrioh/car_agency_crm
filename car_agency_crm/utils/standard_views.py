from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

def list_view(model, model_serializer, request, page_size):
    qs = model.objects.all().order_by('-id')

    paginator = PageNumberPagination()
    paginator.page_size = page_size

    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = model_serializer(paginated_qs, many=True)

    return paginator.get_paginated_response(serializer.data)


def create_view(model_serializer, request, error_message = 'There was an error while creating this object'):
    serializer = model_serializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)

    return Response({"message": error_message}, status=400)


def delete_view(model, obj_id, success_message = 'Object deleted successfully'):
    qs = model.objects.filter(id=obj_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()
    obj.delete()

    return Response({"message": success_message}, status=200)


def edit_view(model, model_serializer, request, obj_id, error_message = 'There was an error while editing this object'):
    qs = model.objects.filter(id=obj_id)

    if not qs.exists():
        return Response({}, status=404)

    obj = qs.first()

    serializer = model_serializer(obj, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=202)

    return Response({"message": error_message}, status=400)