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


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.admin_user)
        except exceptions.ObjectDoesNotExist:
            return False


class IsGroupMember(permissions.BasePermission):
    """Allows access only to users who are members of the specified group."""

    def has_object_permission(self, request, view, obj):
        try:
            if not request.user or not request.user.is_authenticated:
                return False

            if obj.group is None:
                return False

            return request.user.groups.filter(pk=obj.group.pk).exists()
        except exceptions.ObjectDoesNotExist:
            return False
