from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('smrithi/',smrithi,name='smrithi'),
    path('harman/',harman,name='harman'),
]