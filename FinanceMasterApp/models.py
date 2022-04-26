from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Asset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    asset = models.CharField(max_length=50)
    exchange = models.CharField(max_length=50)
    qty = models.DecimalField(max_digits=9,decimal_places=2)
    price = models.DecimalField(max_digits=30,decimal_places=2)
    
    @property
    def total(self):
        return self.qty * self.price


    def __str__(self):
        return self.asset


    class Meta:
        ordering = ['-price']