from rest_framework import permissions


class IsPrivelegesToAccessAsdos(permissions.BasePermission):
    """
    Permission class to access asdos
    """
    def has_permission(self, request, view):
        return request.user.is_admin() or \
               request.user.is_dosen()
