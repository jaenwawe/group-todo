from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FriendsList

User = get_user_model()


@receiver(post_save, sender=User)
def create_friends_list(sender, instance, created, **kwargs):
    if created:
        FriendsList.objects.create(user=instance)
        print('friends list created!')
