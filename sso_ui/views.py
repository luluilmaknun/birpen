"""SSO UI views module."""
from django.shortcuts import render

from rest_framework_jwt.settings import api_settings

def create_token(request):
    response = {'token' : ''}

    if request.user.is_authenticated:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(request.user)
        token = jwt_encode_handler(payload)

        response['token'] = str(token)
        return render(request, 'save_token.html', response)

    return render(request, 'save_token.html', response)
