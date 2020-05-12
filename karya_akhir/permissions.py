from rest_framework import permissions

class IsPrivilegedToReadDataKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        username = view.kwargs.get('username', None)

        return request.user.is_admin() or \
               (request.user.is_mahasiswa() and request.user.username == username)
