from rest_framework import permissions


class IsPrivilegedToAccessAdmin(permissions.BasePermission):
    """
    Permission class to access admin
    """
    def has_permission(self, request, view):
        return request.user.is_admin()
