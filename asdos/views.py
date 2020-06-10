from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import DataError, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from .models import AsistenDosen
from .serializers import AsistenDosenSerializer
from .permissions import IsPrivilegedToAccessAsdos

ASDOS_NOT_FOUND_MESSAGE = 'Data Asisten tidak ditemukan'


@api_view(["GET"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAsdos))
def read_all_asdos(request):
    all_asisten_dosen = AsistenDosen.objects.all().order_by('username')

    all_asisten_dosen_serialized = (AsistenDosenSerializer(asisten_dosen).data \
        for asisten_dosen in all_asisten_dosen)

    return Response({
        "success": True,
        "asisten_dosen": all_asisten_dosen_serialized
    }, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAsdos,))
def create_asisten(request):

    asisten = AsistenDosen()

    try:
        asisten.username = request.data.get('username')

        if asisten.username is None or asisten.username == '':
            raise ValueError

        asisten.save()

    except (ObjectDoesNotExist, ValueError, TypeError, DataError):
        return Response({
            'detail': 'Username tidak valid',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    except IntegrityError:
        return Response({
            'detail': asisten.username + ' sudah terdaftar sebagai asisten.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "detail": 'Data valid',
        "success": True,
    }, status=HTTP_200_OK)


@csrf_exempt
@api_view(["DELETE"])
@permission_classes((IsAuthenticated, IsPrivilegedToAccessAsdos))
def delete_asdos(_, username):

    try:
        asisten = AsistenDosen.objects.get(username=username)
    except AsistenDosen.DoesNotExist:
        return Response({
            'detail': ASDOS_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    asisten.delete()

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
