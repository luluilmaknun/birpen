from rest_framework import permissions


class IsPrivilegedToUpdateAcademicLetterStatus(permissions.BasePermission):
    """
    Permission class to create announcement
    """
    def has_permission(self, request, view):
        return request.user.is_admin()
