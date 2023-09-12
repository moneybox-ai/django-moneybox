from django.urls import path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import SimpleRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from api.views import (
    CurrencyViewSet,
    CurrencyRateViewSet,
    APIUserViewSet,
    ExpenseCategoryViewSet,
    ExpenseViewSet,
    get_token,
    GroupViewSet,
    IncomeCategoryViewSet,
    IncomeViewSet,
    signin,
    signup,
    TransferViewSet,
    WalletViewSet,
)
from api.views.report import ReportViewSet
from moneybox.settings import DEBUG, STATIC_URL, STATIC_ROOT


router = SimpleRouter()

router.register(r"api/v1/user", APIUserViewSet)
router.register(r"api/v1/group", GroupViewSet)
router.register(r"api/v1/wallet", WalletViewSet)
router.register(r"api/v1/incomecategory", IncomeCategoryViewSet)
router.register(r"api/v1/expensecategory", ExpenseCategoryViewSet)
router.register(r"api/v1/income", IncomeViewSet)
router.register(r"api/v1/expense", ExpenseViewSet)
router.register(r"api/v1/transfer", TransferViewSet)
router.register(r"api/v1/currency", CurrencyViewSet)
router.register(r"api/v1/currencyrate", CurrencyRateViewSet)
router.register(r"api/v1/report", ReportViewSet, basename="report")

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

auth_urlpatterns = [
    path("auth/get_token/", get_token),
    path("auth/signup/", signup),
    path("auth/signin/", csrf_exempt(signin)),
]

urlpatterns = router.urls + docs_urlpatterns + auth_urlpatterns
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
