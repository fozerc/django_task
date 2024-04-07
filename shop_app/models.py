from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.transaction import atomic


class ShopUser(AbstractUser):
    user_wallet = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product_description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)


class Purchase(models.Model):
    customer = models.ForeignKey(ShopUser, on_delete=models.CASCADE, related_name='customer_user')
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='chosen_product')


