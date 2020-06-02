from rest_framework import permissions


class IsPrivilegedToEditDataKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa()


class IsPrivilegedToCreateKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa()


class IsPrivilegedToReadDataKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        username = view.kwargs.get('username', None)

        return request.user.is_admin() or \
               (request.user.is_mahasiswa() and request.user.username == username)


class IsPrivilegedToAccessKaryaAkhir(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_admin()


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin()
