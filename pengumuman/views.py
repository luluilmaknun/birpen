from datetime import datetime

from django.contrib.auth import authenticate
from django.core import serializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from .models import Pengumuman


# Create your views here.


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
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'role': user.user_type},
                    status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def filter_pengumuman(request):
    pengumuman_request = request.GET["tanggal"]
    pengumuman_date = datetime.strptime(pengumuman_request, '%d-%m-%Y').date()
    # if user is admin, return all include soft delete
    if request.user.user_type == 4:
        filter_today = Pengumuman.all_objects.filter(tanggal_kelas__date=pengumuman_date)
        pengumuman_response = serializers.serialize("json", filter_today)
    else:
        filter_today = Pengumuman.objects.filter(tanggal_kelas__date=pengumuman_date)
        pengumuman_response = serializers.serialize("json", filter_today)
    return Response({"pengumuman_response": pengumuman_response}, status=200)
