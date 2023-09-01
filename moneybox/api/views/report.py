from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, Max
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.report import ReportSerializer
from users.models import Profile
from wallet.models.expense import Expense
from wallet.models.income import Income


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
            raise Exception("Произошла ошибка при получении отчета: " + str(e))

    @staticmethod
    def get_user_profile(user):
        try:
            return Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            raise Exception("Профиль не найден для этого пользователя")

    @staticmethod
    def get_start_end_dates(start_date=None, end_date=None):
        if not start_date or not end_date:
            today = datetime.now().date()
            start_of_day = datetime.combine(today, datetime.min.time())
            end_of_day = datetime.combine(today, datetime.max.time())
        else:
            start_of_day = datetime.combine(start_date, datetime.min.time())
            end_of_day = datetime.combine(end_date, datetime.max.time())

        start_of_day = timezone.make_aware(start_of_day)
        end_of_day = timezone.make_aware(end_of_day)

        return start_of_day, end_of_day

    @staticmethod
    def get_total_incomes(profile, start_date=None, end_date=None):
        total_incomes_per = (
            Income.objects.filter(
                created_by=profile, created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date)
            )
            .aggregate(total_incomes=Sum("amount"))
            .get("total_incomes")
            or 0
        )

        total_incomes = (
            Income.objects.filter(created_by=profile).aggregate(total_incomes=Sum("amount")).get("total_incomes") or 0
        )

        return total_incomes_per, total_incomes

    @staticmethod
    def get_total_expenses(profile, start_date=None, end_date=None):
        total_expenses_per = (
            Expense.objects.filter(
                created_by=profile, created_at__range=ReportViewSet.get_start_end_dates(start_date, end_date)
            )
            .aggregate(total_expenses=Sum("amount"))
            .get("total_expenses")
            or 0
        )

        total_expenses = (
            Expense.objects.filter(created_by=profile).aggregate(total_expenses=Sum("amount")).get("total_expenses")
            or 0
        )

        return total_expenses_per, total_expenses

    @staticmethod
    def get_income_expense_ratio(total_incomes_per, total_expenses_per):
        if total_expenses_per != 0:
            income_expense_ratio = total_incomes_per / total_expenses_per
        else:
            income_expense_ratio = "В данном периоде не было расходов"

        return income_expense_ratio

    @staticmethod
    def convert_date(date):
        return date.strftime("%d.%m.%Y %H:%M:%S")

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

        return [{**x, "created_at": ReportViewSet.convert_date(x["created_at"])} for x in category_incomes]

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

        return [{**x, "created_at": ReportViewSet.convert_date(x["created_at"])} for x in category_expenses]

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
