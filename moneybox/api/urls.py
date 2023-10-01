from django.urls import path
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
from api.views.invite import InviteViewSet
from api.views.report import ReportViewSet


router = SimpleRouter()

router.register(r"v1/user", APIUserViewSet)
router.register(r"v1/group", GroupViewSet)
router.register(r"v1/wallet", WalletViewSet)
router.register(r"v1/incomecategory", IncomeCategoryViewSet)
router.register(r"v1/expensecategory", ExpenseCategoryViewSet)
router.register(r"v1/income", IncomeViewSet)
router.register(r"v1/expense", ExpenseViewSet)
router.register(r"v1/transfer", TransferViewSet)
router.register(r"v1/currency", CurrencyViewSet)
router.register(r"v1/currencyrate", CurrencyRateViewSet)
router.register(r"v1/report", ReportViewSet, basename="report")

docs_urlpatterns = [
    path("v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "v1/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "v1/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("v1/invite/", InviteViewSet.as_view({"post": "invite"})),
]

auth_urlpatterns = [
    path("v1/auth/get_token/", get_token),
    path("v1/auth/signup/", signup),
    path("v1/auth/signin/", csrf_exempt(signin)),
]

urlpatterns = router.urls + docs_urlpatterns + auth_urlpatterns
