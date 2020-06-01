from rest_framework import permissions

class IsPrivilegedToAccessKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_admin()


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin()
