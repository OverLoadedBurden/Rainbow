from django.shortcuts import HttpResponse
from django.core.serializers import serialize
from .models import Offer, Product
from random import randint
from json import loads
from django.utils.timezone import datetime
import random


# Create your views here.
def count(request):
    return HttpResponse(serialize('json', len(Offer.objects.all())))


def all(request):
    return HttpResponse(serialize('json', Offer.objects.all()))


def delete(request):
    Offer.objects.get(pk=request.GET.get('pk')).delete()
    return HttpResponse(0)


def get(request):
    offer = None
    offer = Offer.objects.get(product=Product.objects.get(pk=request.GET.get('id'))).offer

    return HttpResponse(offer)


def ranged(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    list = Offer.objects.all()
    return HttpResponse(serialize('json', list[start:end]))


def rand(request):
    items = Offer.objects.all()
    items = list(items)
    ret = []
    size = len(items)
    if size > 10:
        size = 10
    if size > 0:
        for i in range(size):
            item = random.choice(items)
            loc = items.index(item)
            ret.append(item)
            items.pop(loc)
    return HttpResponse(serialize('json', ret))


def create(request):
    map = loads(request.body.decode('UTF-8'))
    Offer.objects.create(
        product=Product.objects.get(['name', map['product']])
        , offer=map['offer']
        , end_time=datetime(map['date']['year'], map['date']['month'], map['date']['day'])
    ).save()
    return HttpResponse(0)
