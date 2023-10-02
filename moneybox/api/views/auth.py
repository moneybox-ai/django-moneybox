from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.constants import DEFAULT_INCOME_CATEGORY, DEFAULT_EXPENSE_CATEGORY, WALLET_LIST
from api.encryption import decrypt_ciphertext, encrypt_token
from api.serializers import APIUserSerializer, SignupSerializer
from moneybox.settings import AUTH_HEADER
from users.models import APIUser
from wallet.models.currency import Currency
from wallet.models.group import Group
from wallet.models.income import IncomeCategory
from wallet.models.expense import ExpenseCategory
from wallet.models.wallet import Wallet


@extend_schema(request=SignupSerializer, responses=APIUserSerializer, tags=["Auth"])
@api_view(("POST",))
@permission_classes((AllowAny,))
@transaction.atomic
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        invite_code = serializer.validated_data.get("invite_code")
        user = serializer.save()
        token_for_user = decrypt_ciphertext(user.token)
        if not invite_code:
            group = Group.objects.create()
            group.members.add(user)
            currency = Currency.objects.create(code="RUB", name="Российский рубль")

            expense_categories = [
                ExpenseCategory(name=expense_category, group=group, created_by=user)
                for expense_category in DEFAULT_EXPENSE_CATEGORY
            ]
            print(expense_categories)
            ExpenseCategory.objects.bulk_create(expense_categories)

            income_categories = [
                ExpenseCategory(name=income_category, group=group, created_by=user)
                for income_category in DEFAULT_INCOME_CATEGORY
            ]
            IncomeCategory.objects.bulk_create(income_categories)

            wallets = [
                Wallet(
                    name=wallet,
                    balance=0,
                    group=group,
                    created_by=user,
                    currency=currency,
                )
                for wallet in WALLET_LIST
            ]
            Wallet.objects.bulk_create(wallets)

        return Response({"token": token_for_user}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=APIUserSerializer, responses=None, tags=["Auth"])
@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):
    token_passed = request.data["token"]
    token_db = encrypt_token(token_passed.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)


@extend_schema(request=None, responses=APIUserSerializer, tags=["Auth"])
@api_view(("GET",))
def get_token(request):
    auth_header = request.headers[AUTH_HEADER]
    token_header = auth_header.split(" ")[1]
    token_db = encrypt_token(token_header.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response({"token": token_header}, status.HTTP_200_OK)
