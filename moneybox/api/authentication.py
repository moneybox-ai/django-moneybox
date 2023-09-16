from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import APIUser


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if request.headers.get("Authorization") is not None:
            auth_header = request.headers.get("Authorization")
            header_content = auth_header.split(" ")
            if len(header_content) != 2:
                raise exceptions.AuthenticationFailed("Authorization header should contain 'Token <token_value>'.")
            token_from_header = header_content[1]
            if APIUser.objects.filter(token=token_from_header).exists():
                authenticated_user = APIUser.objects.filter(token=token_from_header).first()
                token = authenticated_user.token
                return (authenticated_user, token)
            raise exceptions.AuthenticationFailed("No such token found.")
        return None
