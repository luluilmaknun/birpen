from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def pengumuman_placeholder_views(_):
    result = {
        "message": "pengumuman placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)
    