from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import DataError, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST
)
from .permissions import IsPrivilegedToAccessAlumni
from .serializers import AlumniSerializer

User = get_user_model()

@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAlumni))
def read_all_alumni(_):
    all_alumni = User.objects.filter(profile__role='alumni').order_by('username')

    all_alumni_serialized = (AlumniSerializer(alumni).data \
        for alumni in all_alumni)

    return Response({
        "success": True,
        "alumni": all_alumni_serialized
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):

    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    try:
        if is_empty(username) or is_empty(password) or \
            is_empty(email):
            raise ValueError

        #Alumni's username must start with @ character
        if username[0] != '@':
            raise ValueError

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

    except (DataError, ValueError):
        return Response({
            'detail': 'Invalid username, email, or password.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    except IntegrityError:
        return Response({
            'detail': 'Username is already registered.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    user.profile.role = 'alumni'
    user.profile.save()

    return Response({
        "success": True,
    }, status=HTTP_200_OK)

def is_empty(field):
    return field is None or field == ''

@csrf_exempt
@api_view(["PATCH"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAlumni))
def update_block_status(request, username):

    blocked = request.data.get('blocked')

    try:
        user = User.objects.get(username=username)
        if not user.is_alumni():
            raise ObjectDoesNotExist

        user.blocked = blocked
        user.save()

    except ObjectDoesNotExist:
        return Response({
            'detail': 'Alumni does not exist.'
        }, status=HTTP_400_BAD_REQUEST)

    except (ValidationError, IntegrityError):
        return Response({
            'detail': 'Invalid data.'
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
