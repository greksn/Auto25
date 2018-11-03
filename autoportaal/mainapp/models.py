from django.db import models
from django.contrib.auth.models import User


class Custom_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length =254)
    last_visted = models.CharField(max_length=200)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    gear_box = models.CharField(max_length=200)
    fuel = models.CharField(max_length=200)
    year = models.IntegerField(default=0)