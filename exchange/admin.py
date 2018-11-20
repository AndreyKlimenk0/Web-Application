from django.contrib import admin
from django.contrib.admin import ModelAdmin
from exchange.models import Provide, Account, Pair, Trade, Order


@admin.register(Provide)
class ProvideAdmin(ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    list_display = ('time', 'key', 'secret')
    fields = ('time', 'key', 'secret', 'user', 'provide')


@admin.register(Pair)
class PairAdmin(ModelAdmin):
    list_display = ('name', 'type_trade')


@admin.register(Trade)
class TradeAdmin(ModelAdmin):
    list_display = ('amount', 'price', 'time')


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('amount', 'price', 'time')
