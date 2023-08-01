from django.urls import path
from app2.views import *
app_name='Nani'
urlpatterns=[
    path('second/',second,name='second')
  
]