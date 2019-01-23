"""
Definition of models.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone


CURRENCY_STORE_FIELD = getattr(settings,
        'WALLET_CURRENCY_STORE_FIELD', models.BigIntegerField)


class Wallet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    current_balance = CURRENCY_STORE_FIELD(default=0)

    created_at = models.DateTimeField(auto_now_add = True)

    def deposit(self,value):
        
        self.transaction_set.create(
            value = value,
            running_balance = self.current_balance + value)
        self.current_balance += value
        self.save()


    def withdraw(self, value):

        self.transaction_set.create(
            value=-value,
            running_balance = self.current_balance - value)
        self.current_balance -= value
        self.save()


class Transaction(models.Model):
    
    wallet = models.ForeignKey(Wallet)

    value = CURRENCY_STORE_FIELD(default = 0)

    running_balance = CURRENCY_STORE_FIELD(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


