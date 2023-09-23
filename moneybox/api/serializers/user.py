from rest_framework import serializers

from users.models import APIUser


class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = "__all__"
