from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers.report import ReportSerializer
from api.utils import get_category_data, get_start_end_dates, get_total_data
from core.defs.chart_generator import generate_charts
from core.defs.datetime import convert_date_to_standart_format
from core.defs.exeptions import ReportAPIException
from users.models import APIUser
from wallet.models.expense import Expense
from wallet.models.income import Income


@extend_schema(tags=["Reports"])
class ReportViewSet(viewsets.ViewSet):
    serializer_class = ReportSerializer

    @staticmethod
    def list(request):
        user_profile = ReportViewSet.get_user_profile(request.user)
        queryset = ReportViewSet.get_queryset(user_profile)
        serializer = ReportViewSet.serializer_class(queryset, context={"request": request})

        report_data = serializer.data
        return Response({"report_data": report_data})

    @action(detail=False, methods=["get"])
    def html(self, request):
        user_profile = ReportViewSet.get_user_profile(request.user)
        queryset = ReportViewSet.get_queryset(user_profile)
        serializer = ReportViewSet.serializer_class(queryset, context={"request": request})

        report_data = serializer.data

        # Getting the selected dates from the request parameters
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        # Use the get_start_end_dates() function to get the start and end date
        start_of_day, end_of_day = get_start_end_dates(start_date, end_date)

        if start_date == end_date:
            x_axis_data = [convert_date_to_standart_format(start_of_day)]
        else:
            x_axis_data = [convert_date_to_standart_format(start_of_day), convert_date_to_standart_format(end_of_day)]

        chart_html = generate_charts(x_axis_data, report_data)

        return HttpResponse(chart_html, content_type="text/html")

    @staticmethod
    def get_user_profile(user):
        profile = get_object_or_404(APIUser, token=user)
        return profile

    @staticmethod
    def get_total_incomes(group, start_date=None, end_date=None):
        try:
            return get_total_data(group, "income_set", start_date, end_date)
        except Exception as e:
            raise ReportAPIException(detail=f"Error occurred while calculating total incomes: {e}")

    @staticmethod
    def get_total_expenses(group, start_date=None, end_date=None):
        try:
            return get_total_data(group, "expense_set", start_date, end_date)
        except Exception as e:
            raise ReportAPIException(detail=f"Error occurred while calculating total expenses: {e}")

    @staticmethod
    def get_income_expense_ratio(total_incomes_per, total_expenses_per):
        try:
            if total_expenses_per != 0:
                income_expense_ratio = total_incomes_per / total_expenses_per
            else:
                income_expense_ratio = 0
            return income_expense_ratio
        except Exception as e:
            raise ReportAPIException(detail=f"Error occurred while calculating income-expense ratio: {e}")

    @staticmethod
    def get_category_incomes(profile, start_date=None, end_date=None):
        try:
            return get_category_data(profile, Income, start_date, end_date)
        except Exception as e:
            raise ReportAPIException(detail=f"Error occurred while fetching category incomes: {e}")

    @staticmethod
    def get_category_expenses(profile, start_date=None, end_date=None):
        try:
            return get_category_data(profile, Expense, start_date, end_date)
        except Exception as e:
            raise ReportAPIException(detail=f"Error occurred while fetching category expenses: {e}")

    @staticmethod
    def get_queryset(profile, start_date=None, end_date=None):
        total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(profile, start_date, end_date)
        total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(profile, start_date, end_date)

        income_expense_ratio = ReportViewSet.get_income_expense_ratio(total_incomes_per, total_expenses_per)

        queryset = {
            "balance": total_incomes - total_expenses,
            "total_incomes": total_incomes_per,
            "total_expenses": total_expenses_per,
            "income_expense_ratio": income_expense_ratio,
            "category_incomes": ReportViewSet.get_category_incomes(profile, start_date, end_date),
            "category_expenses": ReportViewSet.get_category_expenses(profile, start_date, end_date),
        }

        return queryset
