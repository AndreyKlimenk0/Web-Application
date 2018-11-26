from django.db import models
from django.contrib.auth.models import User


class Provider(models.Model):
    privider_id = models.IntegerField()


class Account(models.Model):
    time = models.IntegerField()
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provide = models.ForeignKey('Provider', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.time, self.key, self.secret)


class Pair(models.Model):
    FILL = 'Fill'
    PART_FILL = 'Part-Fill'
    CANCEL = 'Cancel'
    Pair_FIELD_CHOICES = (
        (FILL, 'Fill'),
        (PART_FILL, 'Part fill'),
        (CANCEL, 'Cancel'),
    )
    name = models.CharField(max_length=50)
    type_trade = models.CharField(max_length=50, choices=Pair_FIELD_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.name, self.type_trade)


class Order(models.Model):
    CELL = 'Cell'
    BY = 'By'
    Order_FILED_CHOICES = (
        (CELL, 'Cell'),
        (BY, 'By'),
    )
    amount = models.IntegerField()
    price = models.FloatField()
    time = models.IntegerField()
    type_order = models.CharField(max_length=255, choices=Order_FILED_CHOICES)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    pair = models.ForeignKey('Pair', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.amount, self.price, self.time)


class Trade(models.Model):
    amount = models.IntegerField()
    price = models.FloatField()
    time = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.time, self.amount, self.price)
