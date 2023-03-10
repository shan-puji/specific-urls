from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sanvi(request):
    return HttpResponse('<h1>Sanvi is my bestfriend</h1>')
