from django.db import models

# Create your models here.

class PointShop(models.Model):
    product_name = models.CharField(max_length=256, verbose_name="상품 이름")
    price = models.PositiveIntegerField(verbose_name="상품 가격")