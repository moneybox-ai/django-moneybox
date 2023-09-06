from django.contrib.auth.management.commands import createsuperuser


class CustomSuperuserCommand(createsuperuser.Command):
    ...
