from django.core import exceptions
from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    """Allows access only to authenticated users."""

    def has_permission(self, request, view):
        token = request.auth
        return bool(request.user and token)


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allows unsafe methods to be performed only by administrators."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            request.user.user_for_admin_site
        except exceptions.ObjectDoesNotExist:
            return False
        return bool(request.user and request.user.user_for_admin_site.is_staff)
