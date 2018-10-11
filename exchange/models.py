from django.db import models
from django.contrib.auth.models import User


class Provide(models.Model):
    pass


class Account(models.Model):
    time = models.IntegerField()
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provide = models.ForeignKey('Provide', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.time, self.key, self.secret)


class Pair(models.Model):
    FILL = 'Fill'
    PART_FILL = 'Part-Fill'
    CANCEL = 'Cancel'
    FIELD_CHOICES = (
        (FILL, 'Заполнить'),
        (PART_FILL, 'Неполное заполнение'),
        (CANCEL, 'Отменить')
    )
    name = models.CharField(max_length=50)
    type_trade = models.CharField(max_length=50, choices=FIELD_CHOICES)

    def __str__(self):
        return '{}, {}'.format(self.name, self.type_trade)


class Order(models.Model):
    amount = models.IntegerField()
    price = models.FloatField()
    time = models.IntegerField()
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    pair = models.ForeignKey('Pair', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.amount, self.price, self.time)


class Trade(models.Model):
    amount = models.IntegerField()
    price = models.FloatField()
    time = models.IntegerField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.time, self.amount, self.price)




