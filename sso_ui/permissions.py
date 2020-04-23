from rest_framework import permissions


class isAdmin(permissions.BasePermission):
    """
    Permission class for admin
    """
    def has_permission(self, request, view):
        return request.user.is_admin()


class isDosen(permissions.BasePermission):
    """
    Permission class for dosen
    """
    def has_permission(self, request, view):
        return request.user.is_dosen()


class isAsdos(permissions.BasePermission):
    """
    Permission class for asdos
    """
    def has_permission(self, request, view):
        return request.user.is_asdos()

class IsNotBlocked(permissions.BasePermission):
    """
    Permission class for not blocked user
    """

    message = 'Account has been blocked by administrator.'

    def has_permission(self, request, view):
        return not request.user.is_blocked()
