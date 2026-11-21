from django.shortcuts import render
from django.http import HttpResponse

def add_album(request):
    return HttpResponse("Test")

def load_album(request):
    return HttpResponse("Test")