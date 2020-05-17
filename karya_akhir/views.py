from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
)

from .models import ProgramStudi
from .permissions import IsPrivilegedToAccessKaryaAkhir
from .serializers import ProgramStudiSerializer

@api_view(["GET"])
def karya_akhir_placeholder_views(_):
    result = {
        "message": "karya akhir placeholder message"
    }

    return Response({"success": True, "result": result}, status=HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated, IsPrivilegedToAccessKaryaAkhir])
def read_program_studi(_):
    all_program_studi = ProgramStudi.objects.all()

    return Response({
        "program_studi": (ProgramStudiSerializer(program_studi).data
                          for program_studi in all_program_studi),
    })
