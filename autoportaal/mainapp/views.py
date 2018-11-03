from django.http import HttpResponseRedirect
from django.utils import translation
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.urls import reverse


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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form_title = form.cleaned_data['title']
            form_text = form.cleaned_data['text']
            p = Article(title=form_title, text=form_text)
            p.save()
            # redirect to a new URL:
            messages.success(request, 'Uudis edukalt lisatud!')
            return HttpResponseRedirect(reverse('uudised'))

    # if a GET (or any other method) we'll create a blank form
    else:
        articles = Article.objects.all()
        return render(request, 'mainapp/uudised.html', {'nbar': 'uudised', 'articles': articles})


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
