from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)


@api_view(["GET"])
def alumni_placeholder_views(_):
    result = {
        "message": "alumni placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)
