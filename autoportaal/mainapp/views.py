from django.shortcuts import render

from django.http import HttpResponse

def index (request):
    return render_to_response('mainapp/index.html')