from django.shortcuts import HttpResponse
from json import loads
from .models import *


# Create your views here.
def create(request):
    map = loads(request.body.decode('UTF-8'))
    Request.objects.create(
        user_name=map['name'],
        product=Product.objects.get(pk=map['product']),
        offer_at_the_time=map['offer_at_the_time'],
        color=map['color'],
        size=map['size'],
        count=map['count'],
        credit_card=map['credit_card']
    ).save()
    return HttpResponse('0')
