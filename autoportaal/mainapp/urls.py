from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('uued', views.uued, name='uued'),
    path('foorumid', views.foorumid, name='foorumid'),
    path('uudised', views.uudised, name='uudised'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('add_post', views.add_post, name="add_post"),
    path('language/eng', views.langEng, name="langEng"),
    path('language/est', views.langEst, name="langEst")
]
