from django.db import models

# Create your models here.

class Product(models.Model):
    product = models.CharField('Товар',max_length=30)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')