from django.shortcuts import HttpResponse
from .models import Admin
from json import loads
from django.core.serializers import serialize


# Create your views here.
def auth(request):
    map = loads(request.body.decode('UTF-8'))
    try:
        admin = Admin.objects.get(['name', map['name']])
        if admin.password == map['pass']:
            return HttpResponse(serialize('json', [admin]))
        else:
            return HttpResponse(1)
    except Exception:
        return HttpResponse(2)


def create(request):
    map = loads(request.body.decode('UTF-8'))
    if not map.__contains__('can add'):
        map['can add'] = False
    if not map.__contains__('can delete'):
        map['can delete'] = False
    Admin.objects.create(name=map['name'], password=map['pass'], can_add=map['can add'],
                         can_delete=map['can delete']).save()
    return HttpResponse(0)
