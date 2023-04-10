from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from api import views

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from moneybox.settings import DEBUG, STATIC_URL, STATIC_ROOT


router = SimpleRouter()

router.register(r"api/v1/profile", views.ProfileViewSet)
router.register(r"api/v1/group", views.GroupViewSet)
router.register(r"api/v1/wallet", views.WalletViewSet)
router.register(r"api/v1/incomecategory", views.IncomeCategoryViewSet)
router.register(r"api/v1/expensecategory", views.ExpenseCategoryViewSet)
router.register(r"api/v1/income", views.IncomeViewSet)
router.register(r"api/v1/expense", views.ExpenseViewSet)
router.register(r"api/v1/transfer", views.TransferViewSet)
router.register(r"api/v1/currency", views.CurrencyViewSet)
router.register(r"api/v1/currencyrate", views.CurrencyRateViewSet)

docs_urlpatterns = [
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns = router.urls + docs_urlpatterns
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
