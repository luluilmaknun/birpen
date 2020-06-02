from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError, DataError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)

from .permissions import IsPrivilegedToReadDataKaryaAkhir, IsPrivilegedToAccessKaryaAkhir, \
    IsPrivilegedToCreateKaryaAkhir, IsAdmin
from .models import DataKaryaAkhir, SuratKaryaAkhir, ProgramStudi, JenisKaryaAkhir
from .serializers import DataKaryaAkhirSerializer, SuratKaryaAkhirSerializer, \
    ProgramStudiSerializer, MahasiswaKaryaAkhirSerializer

@api_view(["GET"])
def karya_akhir_placeholder_views(_):
    result = {
        "message": "karya akhir placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdmin])
def read_mahasiswa_karya_akhir(_):
    all_data_karya_akhir = DataKaryaAkhir.objects.all()

    return Response({
        "mahasiswa_karya_akhir": [MahasiswaKaryaAkhirSerializer(data_karya_akhir).data
                                  for data_karya_akhir in all_data_karya_akhir],
    }, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsAdmin])
def filter_mahasiswa(request):
    request_angkatan = request.GET["angkatan"]
    request_prodi = request.GET["prodi"]

    if request_angkatan and request_prodi:
        filtered_data_karya_akhir = DataKaryaAkhir.objects \
            .filter(mahasiswa__profile__year_of_entry=request_angkatan) \
            .filter(mahasiswa__profile__study_program=request_prodi)
    elif not request_prodi and not request_angkatan:
        filtered_data_karya_akhir = DataKaryaAkhir.objects.all()
    elif not request_angkatan:
        filtered_data_karya_akhir = DataKaryaAkhir.objects \
            .filter(mahasiswa__profile__study_program=request_prodi)
    else:
        filtered_data_karya_akhir = DataKaryaAkhir.objects \
            .filter(mahasiswa__profile__year_of_entry=request_angkatan)

    if not filtered_data_karya_akhir:
        return Response({
            "detail": "Tidak ada data yang tersedia"
        }, status=HTTP_200_OK)

    return Response({
        "mahasiswa_karya_akhir": [MahasiswaKaryaAkhirSerializer(surat_karya_akhir).data
                                  for surat_karya_akhir in filtered_data_karya_akhir],
    }, status=HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsPrivilegedToCreateKaryaAkhir])
def create_data_karya_akhir(request):
    if DataKaryaAkhir.objects.filter(mahasiswa=request.user):
        return Response({
            "success": False,
            "detail": "User sudah memiliki data karya akhir",
        }, status=HTTP_400_BAD_REQUEST)

    data_karya_akhir = DataKaryaAkhir()

    data_karya_akhir.mahasiswa = request.user
    try:
        data_karya_akhir.peminatan_mahasiswa = request.data.get('peminatan_mahasiswa')
        data_karya_akhir.jenis_karya_akhir = \
            JenisKaryaAkhir.objects.get(nama=request.data.get('jenis_karya_akhir'))
        data_karya_akhir.sks_diperoleh = request.data.get('sks_diperoleh')
        data_karya_akhir.pembimbing = request.data.get('pembimbing')
        data_karya_akhir.pembimbing_pendamping = request.data.get('pembimbing_pendamping')
        data_karya_akhir.judul_karya_id = request.data.get('judul_karya_id')
        data_karya_akhir.judul_karya_en = request.data.get('judul_karya_en')
        data_karya_akhir.save()

    except (ObjectDoesNotExist, IntegrityError, DataError, ValueError):
        return Response({
            "success": False,
            "detail": "Data tidak valid",
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)


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
