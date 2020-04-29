from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import Pesanan, StatusBayar
from .permissions import IsPrivilegedToUpdateAcademicLetterStatus

@api_view(["GET"])
def permohonan_surat_placeholder_views(_):
    result = {
        "message": "permohonan surat placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)

@csrf_exempt
@api_view(["PATCH"])
@permission_classes((IsAuthenticated, IsPrivilegedToUpdateAcademicLetterStatus))
def update_status_bayar(request, id_pesanan):

    try:
        pesanan = Pesanan.objects.get(pk=id_pesanan)
        status_bayar = StatusBayar.objects.get(nama=request.data.get("status_bayar"))

    except Pesanan.DoesNotExist:
        return Response({
            'detail': 'Data pesanan tidak ditemukan.'
        }, status=HTTP_400_BAD_REQUEST)

    except StatusBayar.DoesNotExist:
        return Response({
            'detail': 'Data status bayar tidak ditemukan.'
        }, status=HTTP_400_BAD_REQUEST)

    pesanan.status_bayar = status_bayar
    pesanan.save()

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
