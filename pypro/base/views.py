from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Olá Django')
# Create your views here.
