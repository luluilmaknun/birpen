from rest_framework import permissions

class IsPrivilegedToCreateKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa()
