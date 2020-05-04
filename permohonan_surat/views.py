from django.core.exceptions import ObjectDoesNotExist, FieldError
from django.core.validators import ValidationError
from django.db.utils import IntegrityError, DataError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import Pesanan, PesananSuratAkademik, SuratAkademik, StatusBayar
from .models import StatusSurat
from .permissions import IsPrivilegedToRequestAcademicLetter, \
    IsPrivilegedToUpdateAcademicLetterStatus
from .serializers import StatusSuratSerializers


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


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated, IsPrivilegedToRequestAcademicLetter,))
def create_pesanan_surat_akademik(request):
    pesanan = Pesanan()
    try:
        pesanan.pemesan = request.user

        if pesanan.pemesan.is_mahasiswa():
            pesanan.nama_pemesan = \
                pesanan.pemesan.first_name + ' ' + pesanan.pemesan.last_name
            pesanan.npm_pemesan = pesanan.pemesan.profile.npm
        else:
            pesanan.nama_pemesan = request.data.get('nama_pemesan')
            pesanan.npm_pemesan = request.data.get('npm_pemesan')

        pesanan.save()

        for surat in request.data.get('surat_akademik'):
            pesanan_surat_akademik = PesananSuratAkademik()
            pesanan_surat_akademik.pesanan = pesanan
            pesanan_surat_akademik.surat_akademik = \
                SuratAkademik.objects.get(jenis_dokumen=surat['jenis_dokumen'])
            pesanan_surat_akademik.jumlah = surat['jumlah']
            pesanan_surat_akademik.full_clean()
            pesanan_surat_akademik.save()

    except (ObjectDoesNotExist, IntegrityError, DataError,
            ValidationError, KeyError, TypeError):
        return Response({
            "success": False,
            'detail': 'Data tidak valid',
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToUpdateAcademicLetterStatus,))
def get_status_surat(request):
    status_surat = StatusSurat.objects.all()
    return Response({
        "success": True,
        "status_surat": StatusSuratSerializers(status_surat, many=True).data,
    }, status=HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes((IsAuthenticated, IsPrivilegedToUpdateAcademicLetterStatus,))
def update_status_surat(request, id_pesanan, jenis_dokumen):
    status_surat = request.data.get('status_surat')

    try:
        psa = PesananSuratAkademik.objects.get(
            pesanan=id_pesanan,
            surat_akademik__jenis_dokumen=jenis_dokumen,
        )
        psa.status_surat.nama = status_surat
        psa.save()

    except (ObjectDoesNotExist, FieldError):
        return Response({
            'detail': 'Pesanan surat/jenis dokumen akademik tidak ditemukan.'
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
