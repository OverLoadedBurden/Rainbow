from django.conf.urls import url
from .views import *

urlpatterns = [
    url('rand', rand),
    url('all', all),
    url('delete', delete),
    url('create/', create),
    url('count', count),
    url('get', get),
    url('ranged/', ranged)
]
