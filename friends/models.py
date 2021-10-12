from django.conf import settings
from django.db import models


class FriendsList(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='friends')


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_user')
    accepted = models.BooleanField(default=False)
