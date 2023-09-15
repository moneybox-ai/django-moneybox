from django.contrib.auth.models import AnonymousUser
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
        if isinstance(request.user, AnonymousUser):
            return False
        try:
            request.user.admin_user
        except exceptions.ObjectDoesNotExist:
            return False
        return bool(request.user and request.user.admin_user.is_staff)
