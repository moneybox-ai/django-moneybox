from django.urls import path

from core.views import healthcheck

urlpatterns = [
    path("healthcheck/", healthcheck, name="healthcheck"),
]
