from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.report import ReportSerializer
from api.utils import get_category_data, get_start_end_dates
from core.chart_generator import (render_bar_chart, render_pie_chart,
                                  render_charts_to_html)
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
            serializer = ReportViewSet.serializer_class(queryset, context={
                "request": request})

            report_data = serializer.data

            return Response({'report_data': report_data})
        except Exception as e:
            raise ReportAPIException(
                detail=f"Произошла ошибка при получении отчета: {e}")

    @action(detail=False, methods=['get'])
    def html(self, request):
        try:
            user_profile = ReportViewSet.get_user_profile(request.user)
            queryset = ReportViewSet.get_queryset(user_profile)
            serializer = ReportViewSet.serializer_class(queryset, context={
                "request": request})

            report_data = serializer.data

            # Получаем выбранные даты из параметров запроса
            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')

            # Используем функцию get_start_end_dates() для получения начальной и конечной даты
            start_of_day, end_of_day = get_start_end_dates(
                start_date, end_date)

            if start_date == end_date:
                x_axis_data = [convert_date_for_html(start_of_day)]
            else:
                x_axis_data = [convert_date_for_html(start_of_day),
                               convert_date_for_html(end_of_day)]

            # Создаем данные для Диаграммы доходов и расходов
            bar_chart_html = render_bar_chart(x_axis_data, report_data)

            # Создаем данные для Круговых диаграмм
            category_incomes = report_data['category_incomes']
            category_expenses = report_data['category_expenses']

            data1 = [(category['category__name'], category['total_expenses'])
                     for category in category_incomes]
            pie_chart1_html = render_pie_chart(data1, "Доходы по категориям")

            data2 = [(category['category__name'], category['total_expenses'])
                     for category in category_expenses]
            pie_chart2_html = render_pie_chart(data2, "Расходы по категориям")

            chart_html = render_charts_to_html(bar_chart_html, pie_chart1_html,
                                               pie_chart2_html)

            return HttpResponse(chart_html, content_type='text/html')
        except Exception as e:
            raise ReportAPIException(
                detail=f"Произошла ошибка при построении HTML: {e}")

    @staticmethod
    def get_user_profile(user):
        profile = get_object_or_404(Profile, user=user)
        return profile

    @staticmethod
    def get_total_incomes(group, start_date=None, end_date=None):
        total_incomes_per = (
                group.income_set.filter(
                    created_at__range=get_start_end_dates(
                        start_date, end_date))
                .aggregate(total_incomes=Sum("amount"))
                .get("total_incomes")
                or 0
        )

        total_incomes = group.income_set.aggregate(
            total_incomes=Sum("amount")).get("total_incomes") or 0

        return total_incomes_per, total_incomes

    @staticmethod
    def get_total_expenses(group, start_date=None, end_date=None):
        total_expenses_per = (
                group.expense_set.filter(
                    created_at__range=get_start_end_dates(
                        start_date, end_date))
                .aggregate(total_expenses=Sum("amount"))
                .get("total_expenses")
                or 0
        )

        total_expenses = group.expense_set.aggregate(
            total_expenses=Sum("amount")).get("total_expenses") or 0

        return total_expenses_per, total_expenses

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
        total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(
            profile, start_date, end_date)
        total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(
            profile, start_date, end_date)

        income_expense_ratio = ReportViewSet.get_income_expense_ratio(
            total_incomes_per, total_expenses_per)

        results = {
            "balance": total_incomes - total_expenses,
            "total_incomes": total_incomes_per,
            "total_expenses": total_expenses_per,
            "income_expense_ratio": income_expense_ratio,
            "category_incomes": ReportViewSet.get_category_incomes(profile,
                                                                   start_date,
                                                                   end_date),
            "category_expenses": ReportViewSet.get_category_expenses(profile,
                                                                     start_date,
                                                                     end_date),
        }

        return results
