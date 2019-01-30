"""
Definition of models.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date

CURRENCY_STORE_FIELD = getattr(settings,
        'WALLET_CURRENCY_STORE_FIELD', models.BigIntegerField)

class DochodCategory(models.Model):
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.description

class Dochod(models.Model):
    
    dochod_id = models.BigIntegerField(default = 0)
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date = models.DateField(blank = True, null = True)
    category = models.ForeignKey(DochodCategory)
    
    def __str__(self):
        return self.description

    def publish(self):
        self.date = timezone.now()
        self.save()

    def getAmount():
        return amount

    class Meta:
        ordering = ['-description', '-pk']
    
class WydatekCategory(models.Model):
    description = models.CharField(max_length = 1000)
    def __str__(self):
        return self.description

class Wydatek(models.Model):
    wydatek_id = models.BigIntegerField(default = 0)
    description = models.CharField(max_length = 1000)
    amount = models.DecimalField(max_digits = 18, decimal_places=2, default = 0)
    date = models.DateField(blank = True, null = True)
    category = models.ForeignKey(WydatekCategory)

    def __str__(self):
        return self.description

    def publish(self):
        self.date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-description', '-pk']

class Wallet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    listaDochodow=[]
    listaWydatkow=[]

    dochod = models.ManyToManyField(Dochod)
    wydatek = models.ManyToManyField(Wydatek)

    
    current_balance = CURRENCY_STORE_FIELD(default=0)

    created_at = models.DateTimeField(auto_now_add = True)

    def dodajDochod(self,dochod):
        
        listaDochodow.append()
        value = dochod.getAmount()
        self.transaction_set.create(
            value = value,
            running_balance = self.current_balance + value)
        self.current_balance += value
        self.save()


    def dodajWydatek(self, value):

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


