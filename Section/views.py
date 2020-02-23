from django.shortcuts import HttpResponse
from django.core.serializers import serialize
from .models import Section
from random import randint
from json import loads
from base64 import b64decode
import random

# Create your views here.
def count(request):
    return HttpResponse(serialize('json', len(Section.objects.all())))


def all(request):
    return HttpResponse(serialize('json', Section.objects.all()))


def delete(request):
    pk = request.GET.get('pk')
    Section.objects.get(pk=pk).delete()
    return HttpResponse(0)


def ranged(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    list = Section.objects.all()
    return HttpResponse(serialize('json', list[start:end]))


def rand(request):
    items = Section.objects.all()
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
    Section.objects.create(
        name=map['name']
        , img=b64decode(map['img'])
        , desc=map['desc']
    ).save()
    return HttpResponse(0)
