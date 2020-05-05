from django.db.utils import IntegrityError, DataError
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import ValidationError
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import Pesanan, PesananSuratAkademik, SuratAkademik
from .permissions import IsPrivilegedToRequestAcademicLetter, \
    IsPrivilegedToAccessAcademicLetter, IsPrivilegedToGetMahasiswaProfile
from .serializers import SuratAkademikSerializer


@api_view(["GET"])
def permohonan_surat_placeholder_views(_):
    result = {
        "message": "permohonan surat placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)

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
def read_surat_akademik(_):
    surat_akademik = SuratAkademik.objects.all().order_by('jenis_dokumen')

    surat_akademik_serialized = \
        (SuratAkademikSerializer(surat).data for surat in surat_akademik)

    return Response({
        "success": True,
        "surat_akademik": surat_akademik_serialized
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToGetMahasiswaProfile,))
def get_mahasiswa_profile(request):

    return Response({
        "mahasiswa": {
            "nama": request.user.first_name + " " + request.user.last_name,
            "npm": request.user.profile.npm,
        }
    }, status=HTTP_200_OK)
