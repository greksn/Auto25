from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

def login(request):
    return render(request, 'mainapp/login.html')

def uued(request):
    return render(request, 'mainapp/uued.html')
    
def foorumid(request):
    return render(request, 'mainapp/foorumid.html')

def uudised(request):
    return render(request, 'mainapp/uudised.html')