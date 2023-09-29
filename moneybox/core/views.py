from django.http import JsonResponse
from django.db import connection
from drf_spectacular.utils import extend_schema

STATUS_OK = {"status": "ok"}
STATUS_ERROR = {"status": "error"}


@extend_schema(tags=["Technical"])
def healthcheck(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return JsonResponse(STATUS_OK)
    except Exception:
        return JsonResponse(STATUS_ERROR)
