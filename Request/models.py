from django.db import models
from Offer.models import Product, Offer
from django.utils.timezone import now


# from django.contrib


# Create your models here.
class Request(models.Model):
    user_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer_at_the_time = models.FloatField(null=True)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=100)
    count = models.IntegerField()
    credit_card = models.IntegerField()
    date = models.DateTimeField(default=now)
