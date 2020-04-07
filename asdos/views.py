from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def asdos_placeholder_views(_):
    result = {
        "message": "asdos placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)
