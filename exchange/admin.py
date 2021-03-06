from django.contrib import admin
from django.contrib.admin import ModelAdmin
from exchange.models import Account, Pair, Trade, Order, Provider


@admin.register(Provider)
class ProviderAdmin(ModelAdmin):
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
    list_filter = ('time',)


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('amount', 'price', 'time')
