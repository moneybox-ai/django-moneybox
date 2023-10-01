from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from moneybox.settings import DEBUG, STATIC_URL, STATIC_ROOT

from core.urls import urlpatterns as core_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
urlpatterns += core_urlpatterns
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
