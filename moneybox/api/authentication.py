from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import APIUser

AUTH_HEADER = "Authorization"


class APIAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get(AUTH_HEADER)
        if not auth_header:
            return None
        header_content = auth_header.split(" ")
        if len(header_content) != 2:
            raise exceptions.AuthenticationFailed("Authorization header should contain 'Token <token_value>'.")
        token_from_header = header_content[1]
        if not APIUser.objects.filter(token=token_from_header).exists():
            raise exceptions.AuthenticationFailed("No such token found.")
        authenticated_user = APIUser.objects.filter(token=token_from_header).first()
        return authenticated_user, authenticated_user.token
