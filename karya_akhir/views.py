from django.db.utils import IntegrityError, DataError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)

from .models import DataKaryaAkhir, JenisKaryaAkhir
from .permissions import IsPrivilegedToEditDataKaryaAkhir

@api_view(["GET"])
def karya_akhir_placeholder_views(_):
    result = {
        "message": "karya akhir placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)

@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsPrivilegedToEditDataKaryaAkhir])
def edit_data_karya_akhir(request):
    try:
        data_karya_akhir = request.user.data_karya_akhir
        data_karya_akhir.peminatan_mahasiswa = request.data.get('peminatan_mahasiswa')
        data_karya_akhir.jenis_karya_akhir = \
            JenisKaryaAkhir.objects.get(nama=request.data.get('jenis_karya_akhir'))
        data_karya_akhir.sks_diperoleh = request.data.get('sks_diperoleh')
        data_karya_akhir.pembimbing = request.data.get('pembimbing')
        data_karya_akhir.pembimbing_pendamping = request.data.get('pembimbing_pendamping')
        data_karya_akhir.judul_karya_id = request.data.get('judul_karya_id')
        data_karya_akhir.judul_karya_en = request.data.get('judul_karya_en')
        data_karya_akhir.save()

    except DataKaryaAkhir.DoesNotExist:
        return Response({
            "success": False,
            "detail": "Data karya akhir untuk " + request.user.username + " tidak ditemukan",
        }, status=HTTP_400_BAD_REQUEST)

    except (JenisKaryaAkhir.DoesNotExist,
            IntegrityError, DataError, ValueError):
        return Response({
            "success": False,
            "detail": "Data tidak valid",
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
