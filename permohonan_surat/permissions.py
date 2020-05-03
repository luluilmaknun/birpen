from rest_framework import permissions


class IsPrivilegedToUpdateAcademicLetterStatus(permissions.BasePermission):
    """
    Permission class to create announcement
    """
    def has_permission(self, request, view):
        return request.user.is_admin()


class IsPrivilegedToRequestAcademicLetter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_mahasiswa() or \
               request.user.is_alumni()
