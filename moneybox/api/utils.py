from datetime import datetime

from django.db.models import Sum, Max
from django.utils import timezone

from core.defs.datetime import convert_date_for_json
from core.defs.exeptions import ReportAPIException


def get_start_end_dates(start_date=None, end_date=None):
    try:
        if not start_date or not end_date:
            today = timezone.now().date()
            start_of_day = timezone.make_aware(datetime.combine(today, datetime.min.time()))
            end_of_day = timezone.make_aware(datetime.combine(today, datetime.max.time()))
        else:
            start_of_day = timezone.make_aware(datetime.combine(start_date, datetime.min.time()))
            end_of_day = timezone.make_aware(datetime.combine(end_date, datetime.max.time()))

        return start_of_day, end_of_day
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while getting start and end dates: {e}")


def get_category_data(profile, model, start_date=None, end_date=None):
    try:
        category_data = (
            model.objects.filter(created_by=profile, created_at__range=get_start_end_dates(start_date, end_date))
            .values("category__name")
            .annotate(total_expenses=Sum("amount"), created_at=Max("created_at"))
            .values("category__name", "total_expenses", "created_at")
        )

        return [{**x, "created_at": convert_date_for_json(x["created_at"])} for x in category_data]
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while fetching category data: {e}")


def get_total_data(group, model, start_date=None, end_date=None):
    try:
        total_data_per = (
            getattr(group, model)
            .filter(created_at__range=get_start_end_dates(start_date, end_date))
            .aggregate(total_data=Sum("amount"))
            .get("total_data")
            or 0
        )

        total_data = getattr(group, model).aggregate(total_data=Sum("amount")).get("total_data") or 0

        return total_data_per, total_data
    except Exception as e:
        raise ReportAPIException(detail=f"Error occurred while calculating total data: {e}")
