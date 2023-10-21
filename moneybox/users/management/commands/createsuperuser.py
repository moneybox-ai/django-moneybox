from django.contrib.auth.management.commands import createsuperuser
from django.core import exceptions
from django.core.management.base import CommandError

from api.encryption import encrypt_token
from users.models import APIUser


class Command(createsuperuser.Command):
    def add_arguments(self, parser):
        parser.add_argument(
            "--token", help="Specifies the token (if any) to be added to the superuser's profile.", required=False
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        user_data = {}
        if options.get("token") is not None:
            new_api_user = None
            token = options.get("token")
            token_encrypted = encrypt_token(token.encode())
            if not APIUser.objects.filter(token=token_encrypted).exists():
                raise CommandError("No such token found.")
            api_user = APIUser.objects.filter(token=token_encrypted).first()
            try:
                api_user.admin_user
            except exceptions.ObjectDoesNotExist:
                new_api_user = api_user
            if new_api_user is None:
                raise CommandError("This token is already taken.")

            user_data["new_api_user"] = new_api_user
        return super().handle(*args, user_data=user_data, **options)
