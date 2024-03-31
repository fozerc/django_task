from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    user_wallet = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_description = models.TextField(null=True, blank=True)
