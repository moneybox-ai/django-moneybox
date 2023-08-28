from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Фllows unsafe methods to be performed only by administrators."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
