from rest_framework import permissions


class IsPrivilegedToCreateAnnouncemment(permissions.BasePermission):
    """
    Permission class to create announcement
    """
    def has_permission(self, request, view):
        return request.user.is_admin() or \
               request.user.is_dosen() or \
               request.user.is_asdos()


class IsPrivilegedToAccessAnnouncemment(permissions.BasePermission):
    """
    Permission class to create announcement
    """
    def has_permission(self, request, view):
        return request.user.is_admin() or \
               request.user.is_dosen() or \
               request.user.is_asdos() or \
               request.user.is_mahasiswa()
