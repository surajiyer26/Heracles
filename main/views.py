from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def home(request):
    return HttpResponse('<h2>You are at Home</h2>')
