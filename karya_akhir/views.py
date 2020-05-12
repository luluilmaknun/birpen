from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
)

from .models import DataKaryaAkhir
from .permissions import IsPrivilegedToReadDataKaryaAkhir
from .serializers import DataKaryaAkhirSerializer


@api_view(["GET"])
def karya_akhir_placeholder_views(_):
    result = {
        "message": "karya akhir placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToReadDataKaryaAkhir])
def read_data_karya_akhir_by_username(_, username):
    try:
        data_karya_akhir = DataKaryaAkhir.objects.get(mahasiswa__username=username)

    except DataKaryaAkhir.DoesNotExist:
        return Response({
            "detail": "Data karya akhir tidak ditemukan.",
        }, status=HTTP_404_NOT_FOUND)

    return Response({
        "data_karya_akhir": DataKaryaAkhirSerializer(data_karya_akhir).data
    }, status=HTTP_200_OK)
