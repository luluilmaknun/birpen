from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)

ASDOS_NOT_FOUND_MESSAGE = 'Asdos does not exist.'


@api_view(["GET"])
def asdos_placeholder_views(_):
    result = {
        "message": "asdos placeholder message"
    }

    return Response({"success": True, "result": result}, status=200)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def delete_asdos(request, key):
    try:
        asdos = Asdos.objects.get(pk=key)
    except Asdos.DoesNotExist:
        return Response({
            'detail': ASDOS_NOT_FOUND_MESSAGE
        }, status=HTTP_400_BAD_REQUEST)

    asdos.delete()

    return Response({
        "success": True,
    }, status=HTTP_200_OK)
