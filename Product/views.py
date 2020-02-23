from django.shortcuts import HttpResponse
from django.core.serializers import serialize
import random
from Section.models import Section
from .models import Product
from random import randint
from json import loads
from base64 import b64decode


# Create your views here.
def count(request):
    return HttpResponse(serialize('json', len(Product.objects.all())))


def delete(request):
    pk = request.GET.get('pk')
    Product.objects.get(pk=pk).delete()
    return HttpResponse(0)


def all(request):
    return HttpResponse(serialize('json', Product.objects.all()))

def section(request):
    return HttpResponse(serialize('json', Product.objects.filter(section=Section.objects.get(name=request.GET.get('name')))))


def get(request):
    return HttpResponse(serialize('json', [Product.objects.get(pk=request.GET.get('pk'))]))


def ranged(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    list = Product.objects.all()
    return HttpResponse(serialize('json', list[start:end]))


def rand(request):
    items = Product.objects.all()
    items=list(items)
    ret = []
    size = len(items)
    if size > 10:
        size = 10
    if size > 0:
        for i in range(size):
            item=random.choice(items)
            loc = items.index(item)
            ret.append(item)
            items.pop(loc)
    return HttpResponse(serialize('json', ret))


def create(request):
    map = loads(request.body.decode('UTF-8'))
    Product.objects.create(
        name=map['name']
        , img=b64decode(map['img'])
        , cost=map['cost']
        , desc=map['desc']
        , section=Section.objects.get(['name', map['section']])
    ).save()
    return HttpResponse(0)
    # print(Section.objects.get(['name', map['section']]))
    # return HttpResponse(1)
