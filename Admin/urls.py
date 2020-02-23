from django.conf.urls import url
from .views import *
urlpatterns = [
    url('auth/', auth),
    url('create/', create),
]
