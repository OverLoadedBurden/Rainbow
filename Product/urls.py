from django.conf.urls import url
from .views import *

urlpatterns = [
    url('rand', rand),
    url('all', all),
    url('get', get),
    url('create/', create),
    url('count', count),
    url('ranged/', ranged),
    url('section/', section),
    url('delete/', delete)
]
