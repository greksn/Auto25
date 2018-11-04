from django.contrib import admin
from .models import User, Post, Article, Thread, ForumPost
# Register your models here.

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Thread)
admin.site.register(ForumPost)