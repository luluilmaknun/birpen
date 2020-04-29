from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import StatusBayar
# Create your views here.

@api_view(["GET"])
def permohonan_surat_placeholder_views(_):
    result = {
        "message": "permohonan surat placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated, ])
def read_status_bayar(request):
    response = {}
    all_obj = StatusBayar.objects.all()

    response["status_bayar"] = [obj.nama for obj in all_obj]

    return Response(response)
