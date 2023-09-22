from django.contrib import admin
from django.urls import include, path

from api.urls import urlpatterns as api_urlpatterns
from core.urls import urlpatterns as core_urlpatterns

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", include(api_urlpatterns))]
urlpatterns += core_urlpatterns
