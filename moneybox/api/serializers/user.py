from rest_framework import serializers

from users.models import APIUser


class APIUserSerializer(serializers.ModelSerializer):
    token = serializers.UUIDField(format="hex_verbose", source="uuid")

    class Meta:
        model = APIUser
        fields = "__all__"
