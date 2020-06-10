from django.db.utils import IntegrityError, DataError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import Admin
from .serializers import AdminSerializer
from .permissions import IsPrivilegedToAccessAdmin

ADMIN_NOT_FOUND_MESSAGE = "Data Admin tidak ditemukan"


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAdmin,))
def read_all_admin(_):
    all_admin = Admin.objects.all().order_by('username')

    all_admin_serialized = (AdminSerializer(admin).data \
        for admin in all_admin)

    return Response({
        "success": True,
        "admin": all_admin_serialized
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAdmin,))
def delete_admin(_, username):
    try:
        admin = Admin.objects.get(username=username)
    except Admin.DoesNotExist:
        return Response({
            "detail": ADMIN_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    admin.delete()

    return Response({
        "success": True,
    }, status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAdmin,))
def create_admin(request):
    username = request.data.get("username")

    if username is None or username == '':
        return Response({
            "detail": "Kolom username kosong"
        }, status=HTTP_400_BAD_REQUEST)

    try:
        Admin.objects.create(username=username)
    except IntegrityError:
        return Response({
            "detail": "Admin sudah terdaftar"
        }, status=HTTP_400_BAD_REQUEST)
    except DataError:
        return Response({
            "detail": "Username tidak valid"
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
