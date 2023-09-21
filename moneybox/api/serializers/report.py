from rest_framework import serializers
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field


class ReportSerializer(serializers.Serializer):
    balance = serializers.SerializerMethodField()
    total_incomes = serializers.SerializerMethodField()
    total_expenses = serializers.SerializerMethodField()
    income_expense_ratio = serializers.SerializerMethodField()
    category_incomes = serializers.SerializerMethodField()
    category_expenses = serializers.SerializerMethodField()

    @staticmethod
    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_balance(obj):
        return obj.get("balance")

    @staticmethod
    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_total_incomes(obj):
        return obj.get("total_incomes")

    @staticmethod
    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_total_expenses(obj):
        return obj.get("total_expenses")

    @staticmethod
    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_income_expense_ratio(obj):
        return obj.get("income_expense_ratio")

    @staticmethod
    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_category_incomes(obj):
        return obj.get("category_incomes")

    @staticmethod
    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_category_expenses(obj):
        return obj.get("category_expenses")
