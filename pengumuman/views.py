from datetime import datetime, timedelta, date

from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
)

from .models import Pengumuman, MataKuliah, JenisPengumuman, \
    Ruang, Sesi, StatusPengumuman
from .permissions import IsPrivilegedToCreateAnnouncemment
from .serializers import PengumumanSerializer

PENGUMUMAN_NOT_FOUND_MESSAGE = 'Pengumuman does not exist.'

@api_view(["GET"])
def pengumuman_placeholder_views(_):
    result = {
        "message": "pengumuman placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated, IsPrivilegedToCreateAnnouncemment,))
def create_pengumuman(request):
    ''' asumsi post buat pengumuman nerima atribut
        atribut yang dipost = atribut pengumuman

        asumsi bentuk tanggal kelas: y-m-d
        asumsi tiap atribut gak ada nama yang sama
    '''
    pengumuman = Pengumuman()
    try:
        pengumuman.pembuat = request.user
        pengumuman.nama_dosen = request.data.get('nama_dosen')
        pengumuman.nama_asisten = request.data.get('nama_asisten')
        pengumuman.komentar = request.data.get('komentar')
        pengumuman.tanggal_kelas = datetime.strptime(
            request.data.get('tanggal_kelas'), '%Y-%m-%d')
        pengumuman.nama_mata_kuliah = MataKuliah.objects.get(
            nama=request.data.get('nama_mata_kuliah'))
        pengumuman.jenis_pengumuman = JenisPengumuman.objects.get(
            nama=request.data.get('jenis_pengumuman'))
        pengumuman.nama_ruang = Ruang.objects.get(
            nama=request.data.get('nama_ruang'))
        pengumuman.nama_sesi = Sesi.objects.get(
            nama=request.data.get('nama_sesi'))
        pengumuman.nama_status_pengumuman = StatusPengumuman.objects.get(
            nama=request.data.get('nama_status_pengumuman'))
    except (ObjectDoesNotExist, ValueError, TypeError):
        return Response({
            'detail': 'Invalid data.',
            "success": False,
        }, status=HTTP_400_BAD_REQUEST)

    pengumuman.save()

    return Response({
        "detail": 'Valid data.',
        "success": True,
        "pengumuman": PengumumanSerializer(pengumuman).data
    }, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_pengumuman_default(request):
    curr_date = date.today()
    tomo_date = curr_date + timedelta(days=1)

    # if user is admin, return all include soft delete
    if request.user.is_admin():
        filter_today = Pengumuman.all_objects.filter(tanggal_kelas__date=curr_date)
        filter_tomo = Pengumuman.all_objects.filter(tanggal_kelas__date=tomo_date)
    else:
        filter_today = Pengumuman.objects.filter(tanggal_kelas__date=curr_date)
        filter_tomo = Pengumuman.objects.filter(tanggal_kelas__date=tomo_date)
    pengumuman_today = (PengumumanSerializer(x).data for x in filter_today)
    pengumuman_tomo = (PengumumanSerializer(x).data for x in filter_tomo)
    return Response({"pengumuman_today": pengumuman_today,
                     "pengumuman_tomo": pengumuman_tomo}, status=200)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def filter_pengumuman(request):
    pengumuman_request = request.GET["tanggal"]
    try:
        pengumuman_date = datetime.strptime(pengumuman_request, '%d-%m-%Y').date()
    except ValueError as err:
        return Response({
            'Error': str(err)
        }, status=HTTP_400_BAD_REQUEST)

    # if user is admin, return all include soft delete
    if request.user.is_admin():
        filter_date = Pengumuman.all_objects.filter(tanggal_kelas__date=pengumuman_date)
    else:
        filter_date = Pengumuman.objects.filter(tanggal_kelas__date=pengumuman_date)
    pengumuman_response = (PengumumanSerializer(x).data for x in filter_date)
    return Response({"pengumuman_response": pengumuman_response}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def edit_pengumuman(request, key):
    try:
        pengumuman = Pengumuman.objects.get(pk=key)
    except Pengumuman.DoesNotExist:
        return Response({
            'detail': PENGUMUMAN_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    if not request.user.is_admin() and pengumuman.pembuat != request.user:
        return Response({
            'detail': 'Not enough privileges.'
        }, status=HTTP_403_FORBIDDEN)

    pengumuman.nama_dosen = request.data.get('nama_dosen')
    pengumuman.nama_asisten = request.data.get('nama_asisten')
    pengumuman.komentar = request.data.get('komentar')

    try:
        pengumuman.tanggal_kelas = datetime.strptime(request.data.get('tanggal_kelas'),
                                                     '%Y-%m-%d')
        pengumuman.nama_mata_kuliah = \
            MataKuliah.objects.get(nama=request.data.get('nama_mata_kuliah'))
        pengumuman.jenis_pengumuman = \
            JenisPengumuman.objects.get(nama=request.data.get('jenis_pengumuman'))
        pengumuman.nama_ruang = Ruang.objects.get(nama=request.data.get('nama_ruang'))
        pengumuman.nama_sesi = Sesi.objects.get(nama=request.data.get('nama_sesi'))
        pengumuman.nama_status_pengumuman = \
            StatusPengumuman.objects.get(nama=request.data.get('nama_status_pengumuman'))
    except (ObjectDoesNotExist, ValueError, TypeError):
        return Response({
            'detail': 'Invalid data.'
        }, status=HTTP_400_BAD_REQUEST)

    pengumuman.save()

    return Response({
        "success": True,
        "pengumuman": PengumumanSerializer(pengumuman).data
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def dropdown_pengumuman(request):
    response = {}
    DROPDOWN = {
        JenisPengumuman: 'jenis_pengumuman',
        MataKuliah: 'mata_kuliah',
        Ruang: 'ruang',
        Sesi: 'sesi',
        StatusPengumuman: 'status_pengumuman'
    }
    for data, key in DROPDOWN.items():
        all_obj = data.objects.all()
        response[key] = [_.nama for _ in all_obj]

    return Response(response)

@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_pengumuman(request, key):
    try:
        pengumuman = Pengumuman.objects.get(pk=key)
    except Pengumuman.DoesNotExist:
        return Response({
            'detail': PENGUMUMAN_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    if pengumuman.pembuat != request.user and not request.user.is_admin():
        return Response({
            'detail': 'You are not the owner of the announcement.'
        }, status=HTTP_403_FORBIDDEN)

    pengumuman.delete()

    return Response({
        "success": True,
        "pengumuman": PengumumanSerializer(pengumuman).data
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def read_pengumuman_by_pk(request, key):
    try:
        if not request.user.is_admin():
            pengumuman = Pengumuman.objects.get(pk=key)
        else:
            pengumuman = Pengumuman.all_objects.get(pk=key)
    except Pengumuman.DoesNotExist:
        return Response({
            'detail': PENGUMUMAN_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
        "pengumuman": PengumumanSerializer(pengumuman).data
    }, status=HTTP_200_OK)
