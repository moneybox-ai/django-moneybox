from datetime import datetime
from django.db.models import Sum, Max
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from api.serializers.report import ReportSerializer
from core.datetime import convert_date
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
            return Response(serializer.data)
        except Exception as e:
            raise ReportAPIException(detail=f"Произошла ошибка при получении отчета: {e}")

    @staticmethod
    def get_user_profile(user):
        profile = get_object_or_404(Profile, user=user)
        return profile

    @staticmethod
    def get_start_end_dates(start_date=None, end_date=None):
        if not start_date or not end_date:
            today = timezone.now().date()
            start_of_day = timezone.make_aware(datetime.combine(today, datetime.min.time()))
            end_of_day = timezone.make_aware(datetime.combine(today, datetime.max.time()))
        else:
            start_of_day = timezone.make_aware(datetime.combine(start_date, datetime.min.time()))
            end_of_day = timezone.make_aware(datetime.combine(end_date, datetime.max.time()))

        return start_of_day, end_of_day

    @staticmethod
    def get_total_incomes(group, start_date=None, end_date=None):
        total_incomes_per = (
            group.income_set.filter(created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date))
            .aggregate(total_incomes=Sum("amount"))
            .get("total_incomes")
            or 0
        )

        total_incomes = group.income_set.aggregate(total_incomes=Sum("amount")).get("total_incomes") or 0

        return total_incomes_per, total_incomes

    @staticmethod
    def get_total_expenses(group, start_date=None, end_date=None):
        total_expenses_per = (
            group.expense_set.filter(created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date))
            .aggregate(total_expenses=Sum("amount"))
            .get("total_expenses")
            or 0
        )

        total_expenses = group.expense_set.aggregate(total_expenses=Sum("amount")).get("total_expenses") or 0

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
        category_incomes = (
            Income.objects.filter(
                created_by=profile, created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date)
            )
            .values("category__name")
            .annotate(total_expenses=Sum("amount"), created_at=Max("created_at"))
            .values("category__name", "total_expenses", "created_at")
        )

        return [{**x, "created_at": convert_date(x["created_at"])} for x in category_incomes]

    @staticmethod
    def get_category_expenses(profile, start_date=None, end_date=None):
        category_expenses = (
            Expense.objects.filter(
                created_by=profile, created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date)
            )
            .values("category__name")
            .annotate(total_expenses=Sum("amount"), created_at=Max("created_at"))
            .values("category__name", "total_expenses", "created_at")
        )

        return [{**x, "created_at": convert_date(x["created_at"])} for x in category_expenses]

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
