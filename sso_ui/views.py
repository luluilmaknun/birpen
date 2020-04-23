"""SSO UI views module."""
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, get_user_model

from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
)

User = get_user_model()

def save_user_info(request):
    response = {'token' : '', 'username':'', 'role':'', 'is_admin':'', 'is_asdos':''}

    if request.user.is_authenticated:
        response['token'] = str(create_token(request.user))
        response['username'] = request.user.username
        response['role'] = request.user.profile.role
        response['is_admin'] = request.user.is_admin()
        response['is_asdos'] = request.user.is_asdos()
        return render(request, 'save_user_info.html', response)

    return render(request, 'save_user_info.html', response)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def obtain_user_info(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response({
            'detail': 'Please provide both username and password.'
        }, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({
            'detail': 'Invalid credentials.'
        }, status=HTTP_401_UNAUTHORIZED)

    if user.is_blocked():
        return Response({
            'detail': 'Account has been blocked by administrator.'
        }, status=HTTP_403_FORBIDDEN)

    return Response({
        'token': str(create_token(user)),
        'username': user.username,
        'role': user.profile.role,
        'is_admin': user.is_admin(),
        'is_asdos': user.is_asdos()
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def refresh_data(request):

    return Response({
        'token': str(create_token(request.user)),
        'username': request.user.username,
        'role': request.user.profile.role,
        'is_admin': request.user.is_admin(),
        'is_asdos': request.user.is_asdos()
    }, status=HTTP_200_OK)

def create_token(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return token
