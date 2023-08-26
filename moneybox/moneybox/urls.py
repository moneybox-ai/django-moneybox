from django.contrib import admin
from django.urls import path, include

from api.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')
         )
]
urlpatterns += api_urlpatterns
