from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from wallet.models.currency import Currency, CurrencyRate


class CurrencySerializer(ModelSerializer):
    code = serializers.CharField(
        validators=(UniqueValidator(queryset=Currency.objects.all()),),
        required=True,
    )
    name = serializers.CharField(
        validators=(UniqueValidator(queryset=Currency.objects.all()),),
        required=True,
    )

    class Meta:
        model = Currency
        fields = ("id", "code", "name", "created_at", "updated_at")
        validators = (
            UniqueTogetherValidator(
                queryset=Currency.objects.all(),
                fields=(
                    "code",
                    "name",
                ),
            ),
        )


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = ("id", "currency", "rate")
