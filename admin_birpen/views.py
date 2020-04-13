from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)

from .models import Admin
from .serializers import AdminSerializer
from .permissions import IsPrivilegedToAccessAdmin


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAdmin,))
def read_all_admin(_):
    all_admin = Admin.objects.all()

    all_admin_serialized = (AdminSerializer(admin).data \
        for admin in all_admin)

    return Response({
        "success": True,
        "admin": all_admin_serialized
    }, status=HTTP_200_OK)
