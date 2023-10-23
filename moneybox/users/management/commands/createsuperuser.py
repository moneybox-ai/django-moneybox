import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.management.commands import createsuperuser
from django.core import exceptions
from django.core.management.base import CommandError

from api.encryption import decrypt_ciphertext, encrypt_token
from users.models import APIUser

User = get_user_model()


class Command(createsuperuser.Command):
    def add_arguments(self, parser):
        parser.add_argument(
            "--token", help="Specifies the token (if any) to be added to the superuser's profile.", required=False
        )
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        if options.get("token") is not None:
            new_api_user_is_created = False
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
        else:
            from api.utils import add_defaults

            new_api_user_is_created = True
            token_new = str(uuid.uuid4())
            token_db = encrypt_token(token_new.encode())
            new_api_user = APIUser.objects.create(token=token_db)

            add_defaults(user=new_api_user)

        super().handle(*args, **options)
        superuser = User.objects.latest("date_joined")
        superuser.api_user = new_api_user
        superuser.save()

        if new_api_user_is_created:
            token = decrypt_ciphertext(superuser.api_user.token)
            self.stdout.write(f"API user added to created superuser; API user token: {token}")
