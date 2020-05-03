from rest_framework import permissions


class IsPrivilegedToRequestAcademicLetter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni()


class IsPrivilegedToEditSurat(permissions.BasePermission):
    """
    Permission class to access admin
    """
    def has_permission(self, request, view):
        return request.user.is_admin()
