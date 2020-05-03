from rest_framework import permissions


class IsPrivilegedToRequestAcademicLetter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni()


class IsPrivilegedToGetMahasiswaProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa()


class IsPrivilegedToAccessAcademicLetter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni() or \
               request.user.is_admin()
