from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
  # return HttpResponse('Welcome')
  # return render (response, 'authentication/register.html')
  return render (response, 'OAuth.html')
