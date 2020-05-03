from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import StatusBayar
from .permissions import IsPrivilegedToUpdateAcademicLetterStatus
from .serializers import StatusBayarSerializer


@api_view(["GET"])
def permohonan_surat_placeholder_views(_):
    result = {
        "message": "permohonan surat placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToUpdateAcademicLetterStatus])
def read_status_bayar(request):
    all_obj = StatusBayar.objects.all()

    return Response({
        "status_bayar": (StatusBayarSerializer(x).data for x in all_obj),
    })
