from django.conf.urls import url
from .views import *

urlpatterns = [
    url('rand', rand),
    url('create/', create),
    url('count', count),
    url('ranged/', ranged),
    url('all/', all),
    url('delete/', delete),
]
