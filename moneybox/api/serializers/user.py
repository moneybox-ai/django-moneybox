from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(format='hex_verbose')

    class Meta:
        model = CustomUser
        fields = "__all__"
