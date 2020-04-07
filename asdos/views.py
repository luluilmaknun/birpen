from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

from sso_ui.models import AsistenDosen
from .permissions import IsPrivelegesToAccessAsdos


@api_view(["GET"])
def asdos_placeholder_views(_):
    result = {
        "message": "asdos placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated, IsPrivelegesToAccessAsdos))
def create_asisten(request):

    asisten = AsistenDosen()

    try:
        asisten.username = request.data.get('username')
        len_uname = len(asisten.username)
        if asisten.username is None or len_uname <= 0 or len_uname > 32:
            raise ValueError

        if (AsistenDosen.objects.filter(username=asisten.username).exists()) is True:
            return Response({
                'detail': asisten.username + ' is already registered as asisten.',
                'success': False,
            }, status=HTTP_400_BAD_REQUEST)

        asisten.save()
    except (ObjectDoesNotExist, ValueError, TypeError):
        return Response({
            'detail': 'Invalid username.',
            'success': False,
        }, status=HTTP_400_BAD_REQUEST)

    return Response({
        "detail": 'Valid data.',
        "success": True,
    }, status=HTTP_200_OK)
