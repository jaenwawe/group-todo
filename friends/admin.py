from django.contrib import admin

from .models import FriendRequest, FriendsList

admin.site.register(FriendRequest)
admin.site.register(FriendsList)
