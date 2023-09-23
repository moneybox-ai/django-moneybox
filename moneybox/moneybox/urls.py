from django.contrib import admin
from django.urls import path

from api.urls import urlpatterns as api_urlpatterns
from core.urls import urlpatterns as core_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += api_urlpatterns
urlpatterns += core_urlpatterns
