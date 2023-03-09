from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<h1><marquee>virat kohli is the chase master and the best batsman in the world</marquee></h1>')
def dhoni(request):
    return HttpResponse('<h2><marquee>Dhoni is the coolest captain</marquee></h2>')