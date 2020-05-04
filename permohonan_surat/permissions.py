from rest_framework import permissions

from .models import Pesanan


class IsPrivilegedToRequestAcademicLetter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni()

class IsPrivilegedToReadPesanan(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni() or \
               request.user.is_admin()

class IsPrivilegedToReadDetailPesanan(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin():
            return True

        id_pesanan = request.resolver_match.kwargs.get('id_pesanan')

        return Pesanan.objects.filter(id=id_pesanan).count() == 1 and \
               Pesanan.objects.get(id=id_pesanan).pemesan == request.user
