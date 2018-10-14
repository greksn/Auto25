from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {'nbar': 'index'})

def login(request):
    return render(request, 'mainapp/login.html', {'nbar': 'login'})

def uued(request):
    return render(request, 'mainapp/uued.html', {'nbar': 'uued'})

def foorumid(request):
    return render(request, 'mainapp/foorumid.html', {'nbar': 'foorumid'})

def uudised(request):
    return render(request, 'mainapp/uudised.html', {'nbar': 'uudised'})

def add_post(request):
    return render(request, 'mainapp/add_post.html',{'nbar': 'add_post'})