"""SSO UI views module."""
from django.shortcuts import render

from rest_framework_jwt.settings import api_settings
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import AsistenDosen

def save_user_info(request):
    response = {'token' : '', 'username':'', 'role':'', 'is_admin':'', 'is_asdos':''}

    if request.user.is_authenticated:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)

        response['token'] = str(token)
        response['username'] = request.user.username
        response['role'] = request.user.profile.role
        response['is_admin'] = request.user.is_admin()
        response['is_asdos'] = request.user.is_asdos()
        return render(request, 'save_user_info.html', response)

    return render(request, 'save_user_info.html', response)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def create_asisten(request):
    if (request.user.is_dosen() or request.user.is_admin()) is False:
        return Response({
            'detail': 'Role is not dosen.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    asisten = AsistenDosen()

    try:
        asisten.username = request.data.get('username')
        if asisten.username is None:
            raise ValueError
        asisten.save()
    except (ObjectDoesNotExist, ValueError, TypeError):
        return Response({
            'detail': 'Invalid data.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)


    return Response({
        "detail": 'Valid data.',
        "success": True,
    }, status=HTTP_200_OK)
    
