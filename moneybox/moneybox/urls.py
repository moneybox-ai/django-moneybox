from django.contrib import admin
from django.urls import path, include

from api.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')
         )
=======
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
>>>>>>> upstream/main
]
urlpatterns += api_urlpatterns
