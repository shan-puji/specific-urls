from app3.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('julia/',julia,name='julia'),
]