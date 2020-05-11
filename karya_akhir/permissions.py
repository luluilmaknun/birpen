from rest_framework import permissions

class IsPrivilegedToEditDataKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa()
