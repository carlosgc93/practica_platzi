from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse("Hola Django")

def hola(request):
    pass