from rest_framework import permissions

class IsNotBlocked(permissions.BasePermission):
    """
    Permission class for not blocked user
    """

    message = 'Account has been blocked by administrator.'

    def has_permission(self, request, view):
        return not request.user.is_blocked()
