from django.db import models
from Product.models import Product


# Create your models here.
class Offer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, primary_key=True)
    offer = models.FloatField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'%{self.offer} Offer on ' + self.product.name
