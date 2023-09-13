from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import APIUser


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get("Authorization") is not None:
            auth_header = request.headers.get("Authorization")
            # Auth header should look like "Token <uuid_string>"
            token_from_header = auth_header.split(" ")[1]
            if APIUser.objects.filter(token=token_from_header).exists():
                authenticated_user = APIUser.objects.filter(token=token_from_header).first()
                token = authenticated_user.token
                return (authenticated_user, token)
            return exceptions.AuthenticationFailed("No such token found.")
        return None
