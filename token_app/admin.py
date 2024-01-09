from django.contrib import admin
from .models import Token, ICO, TokenPurchase, UserWallet


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'total_supply')


@admin.register(ICO)
class ICOAdmin(admin.ModelAdmin):
    list_display = ('token', 'start_date', 'end_date', 'hard_cap', 'soft_cap')


@admin.register(TokenPurchase)
class TokenPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'quantity', 'price', 'date_purchased')


@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
