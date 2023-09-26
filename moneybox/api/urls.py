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
from api.views.invite import InviteViewSet
from api.views.report import ReportViewSet
from moneybox.settings import DEBUG, STATIC_URL, STATIC_ROOT


router = SimpleRouter()

router.register(r"user", APIUserViewSet)
router.register(r"group", GroupViewSet)
router.register(r"wallet", WalletViewSet)
router.register(r"incomecategory", IncomeCategoryViewSet)
router.register(r"expensecategory", ExpenseCategoryViewSet)
router.register(r"income", IncomeViewSet)
router.register(r"expense", ExpenseViewSet)
router.register(r"transfer", TransferViewSet)
router.register(r"currency", CurrencyViewSet)
router.register(r"currencyrate", CurrencyRateViewSet)
router.register(r"report", ReportViewSet, basename="report")

docs_urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("invite/", InviteViewSet.as_view({"post": "invite"})),
]

auth_urlpatterns = [
    path("auth/get_token/", get_token),
    path("auth/signup/", signup),
    path("auth/signin/", csrf_exempt(signin)),
]

urlpatterns = router.urls + docs_urlpatterns + auth_urlpatterns
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
