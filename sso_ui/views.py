"""SSO UI views module."""
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token


def create_token(request):
    if request.user.is_authenticated:
        token, _ = Token.objects.get_or_create(user=request.user)
        return JsonResponse({
            'token' : str(token)
        })
    else:
        return redirect('/')
