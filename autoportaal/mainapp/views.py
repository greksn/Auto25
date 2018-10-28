from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

def langEng(request):
    translation.activate("en-GB")
    request.session[translation.LANGUAGE_SESSION_KEY] = "en-GB"
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def langEst(request):
    translation.activate("et")
    request.session[translation.LANGUAGE_SESSION_KEY] = "et"
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_post(request):
    return render(request, 'mainapp/add_post.html', {'nbar': 'add_post'})
