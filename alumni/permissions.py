from rest_framework import permissions


class IsPrivilegedToAccessAlumni(permissions.BasePermission):
    """
    Permission class to access alumni
    """
    def has_permission(self, request, view):
        return request.user.is_admin()
