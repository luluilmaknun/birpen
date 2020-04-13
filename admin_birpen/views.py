from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)


@api_view(["GET"])
def admin_placeholder_views(_):
    result = {
        "message": "admin birpen placeholder message"
    }

    return Response({
        "success": True,
        "result": result
    }, status=HTTP_200_OK)
