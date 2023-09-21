from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.report import ReportSerializer
from api.utils import get_category_data, get_start_end_dates, get_total_data
from core.chart_generator import generate_charts
from core.datetime import convert_date_for_html
from users.models import Profile
from wallet.models.expense import Expense
from wallet.models.income import Income


class ReportAPIException(APIException):
    def __init__(self, detail, status_code=None):
        super().__init__(detail)
        self.status_code = status_code


class ReportViewSet(viewsets.ViewSet):
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def list(request):
        try:
            user_profile = ReportViewSet.get_user_profile(request.user)
            queryset = ReportViewSet.get_queryset(user_profile)
            serializer = ReportViewSet.serializer_class(queryset, context={"request": request})

            report_data = serializer.data

            return Response({"report_data": report_data})
        except Exception as e:
            raise ReportAPIException(detail=f"Произошла ошибка при получении отчета: {e}")

    @action(detail=False, methods=["get"])
    def html(self, request):
        try:
            user_profile = ReportViewSet.get_user_profile(request.user)
            queryset = ReportViewSet.get_queryset(user_profile)
            serializer = ReportViewSet.serializer_class(queryset, context={"request": request})

            report_data = serializer.data

            # Получаем выбранные даты из параметров запроса
            start_date = request.query_params.get("start_date")
            end_date = request.query_params.get("end_date")

            # Используем функцию get_start_end_dates() для получения начальной и конечной даты
            start_of_day, end_of_day = get_start_end_dates(start_date, end_date)

            if start_date == end_date:
                x_axis_data = [convert_date_for_html(start_of_day)]
            else:
                x_axis_data = [convert_date_for_html(start_of_day), convert_date_for_html(end_of_day)]

            chart_html = generate_charts(x_axis_data, report_data)

            return HttpResponse(chart_html, content_type="text/html")
        except Exception as e:
            raise ReportAPIException(detail=f"Произошла ошибка при построении HTML: {e}")

    @staticmethod
    def get_user_profile(user):
        profile = get_object_or_404(Profile, user=user)
        return profile

    @staticmethod
    def get_total_incomes(group, start_date=None, end_date=None):
        return get_total_data(group, "income_set", start_date, end_date)

    @staticmethod
    def get_total_expenses(group, start_date=None, end_date=None):
        return get_total_data(group, "expense_set", start_date, end_date)

    @staticmethod
    def get_income_expense_ratio(total_incomes_per, total_expenses_per):
        if total_expenses_per != 0:
            income_expense_ratio = total_incomes_per / total_expenses_per
        else:
            income_expense_ratio = 0

        return income_expense_ratio

    @staticmethod
    def get_category_incomes(profile, start_date=None, end_date=None):
        return get_category_data(profile, Income, start_date, end_date)

    @staticmethod
    def get_category_expenses(profile, start_date=None, end_date=None):
        return get_category_data(profile, Expense, start_date, end_date)

    @staticmethod
    def get_queryset(profile, start_date=None, end_date=None):
        total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(profile, start_date, end_date)
        total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(profile, start_date, end_date)

        income_expense_ratio = ReportViewSet.get_income_expense_ratio(total_incomes_per, total_expenses_per)

        results = {
            "balance": total_incomes - total_expenses,
            "total_incomes": total_incomes_per,
            "total_expenses": total_expenses_per,
            "income_expense_ratio": income_expense_ratio,
            "category_incomes": ReportViewSet.get_category_incomes(profile, start_date, end_date),
            "category_expenses": ReportViewSet.get_category_expenses(profile, start_date, end_date),
        }

        return results
