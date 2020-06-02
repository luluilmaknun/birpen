from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)

from .models import DataKaryaAkhir, SuratKaryaAkhir, ProgramStudi
from .permissions import IsPrivilegedToReadDataKaryaAkhir, IsPrivilegedToAccessKaryaAkhir
from .serializers import DataKaryaAkhirSerializer, SuratKaryaAkhirSerializer, \
    ProgramStudiSerializer


@api_view(["GET"])
def karya_akhir_placeholder_views(_):
    result = {
        "message": "karya akhir placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToReadDataKaryaAkhir])
def read_data_karya_akhir_by_username(_, username):
    try:
        data_karya_akhir = DataKaryaAkhir.objects.get(mahasiswa__username=username)

    except DataKaryaAkhir.DoesNotExist:
        return Response({
            "detail": "Data karya akhir tidak ditemukan.",
        }, status=HTTP_404_NOT_FOUND)

    return Response({
        "data_karya_akhir": DataKaryaAkhirSerializer(data_karya_akhir).data
    }, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToAccessKaryaAkhir])
def read_surat_karya_akhir(_):
    all_surat_karya_akhir = SuratKaryaAkhir.objects.all()

    return Response({
        "surat_karya_akhir": (SuratKaryaAkhirSerializer(surat_karya_akhir).data
                              for surat_karya_akhir in all_surat_karya_akhir),
    })

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToAccessKaryaAkhir])
def read_program_studi(_):
    all_program_studi = ProgramStudi.objects.all()

    return Response({
        "program_studi": (ProgramStudiSerializer(program_studi).data
                          for program_studi in all_program_studi),
    })
