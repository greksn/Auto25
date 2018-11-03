from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Custom_user, Post
# Register your models here.

class Custom_userInline(admin.StackedInline):
    model = Custom_user
    can_delete = False
    verbose_name_plural = 'Custom users'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Custom_userInline,)

admin.site.register(User, UserAdmin)
admin.site.register(Post)