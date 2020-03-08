"""SSO UI views module."""
from django.shortcuts import render
from rest_framework.authtoken.models import Token


def create_token(request):
    response = {'token' : ''}

    if request.user.is_authenticated:
        token, _ = Token.objects.get_or_create(user=request.user)
        response['token'] = str(token)
        return render(request, 'save_token.html', response)

    return render(request, 'save_token.html', response)
