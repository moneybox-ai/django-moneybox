from django.contrib import admin
from django.urls import path, include

from core.urls import urlpatterns as core_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
urlpatterns += core_urlpatterns
