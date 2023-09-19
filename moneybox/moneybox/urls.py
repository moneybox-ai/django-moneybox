from django.contrib import admin
from django.urls import path, include

from api.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('api.urls'))
]
urlpatterns += api_urlpatterns
