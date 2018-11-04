from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    gear_box = models.CharField(max_length=200)
    fuel = models.CharField(max_length=200)
    year = models.IntegerField(default=0)

class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)

class Thread(models.Model):
    title = models.CharField(max_length=50)

class ForumPost(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=50)

