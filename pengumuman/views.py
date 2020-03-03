from datetime import datetime

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_403_FORBIDDEN,
    HTTP_401_UNAUTHORIZED
)

from .serializers import PengumumanSerializer
from .models import User, Pengumuman, MataKuliah, JenisPengumuman, \
    Ruang, Sesi, StatusPengumuman


@api_view(["GET"])
def pengumuman_placeholder_views(_):
    result = {
        "message": "pengumuman placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)


@csrf_exempt
@api_view(["POST", "GET"])
@permission_classes((AllowAny,))
def login(request):
    if request.method == "GET":
        response = {}
        return render(request, 'login.html', response)

    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'detail': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'detail': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'role': user.user_type},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def edit_pengumuman(request, key):
    try:
        pengumuman = Pengumuman.objects.get(pk=key)
    except Pengumuman.DoesNotExist:
        return Response({
            'detail': 'Pengumuman does not exist.'
        }, status=HTTP_400_BAD_REQUEST)

    if request.user.user_type != User.ADMIN and pengumuman.pembuat != request.user:
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
