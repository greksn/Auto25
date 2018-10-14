from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name ='login'),
    path('uued', views.uued, name ='uued'),
    path('foorumid', views.foorumid, name ='foorumid'),
    path('uudised', views.uudised, name ='uudised'),
]