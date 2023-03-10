from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def julia(request):
    return HttpResponse('<h1>juliya is also my bestfriend</h1>')
 