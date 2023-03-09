from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def smrithi(request):
    return HttpResponse('<h1><marquee>she is the captain of RCB womens team</marquee></h1>')
def harman(request):
    return HttpResponse('<h2><marquee>she is the captain of MI womens team</marquee></h2>')