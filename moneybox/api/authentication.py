from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from api.encryption import encrypt_token
from moneybox.settings import AUTH_HEADER
from users.models import APIUser


class APIAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get(AUTH_HEADER)
        if not auth_header:
            return None
        header_content = auth_header.split(" ")
        if len(header_content) != 2:
            raise exceptions.AuthenticationFailed("Authorization header should contain 'Token <token_value>'.")
        token_header = header_content[1]
        token_db = encrypt_token(token_header.encode())
        if not APIUser.objects.filter(token=token_db).exists():
            raise exceptions.AuthenticationFailed("No such token found.")
        authenticated_user = APIUser.objects.filter(token=token_db).first()
        return authenticated_user, authenticated_user.token
