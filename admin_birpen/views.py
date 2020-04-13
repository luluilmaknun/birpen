from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import Admin
from .permissions import IsPrivilegedToAccessAdmin

ADMIN_NOT_FOUND_MESSAGE = "Admin does not exist."


@api_view(["GET"])
def admin_placeholder_views(_):
    result = {
        "message": "admin birpen placeholder message"
    }

    return Response({
        "success": True,
        "result": result
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
