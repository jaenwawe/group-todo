from django.conf import settings
from django.db import models


class FriendsList(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        """
        Add a new friend.

        Params:
        account: The User object of the person that will be added to the friend list.
        """

        # Check to see if the account is already friends with the user.
        # If not, then add them to the friend list.
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        """
        Remove an existing friend.

        Params:
        account: The User object of the person that will be removed from the friend list.
        """
        # Check to see if the account is already friends with the user.
        # If they are friends, remove account from friends list.
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """
        Initiate the action of removing a friend. The remover initiates the action.

        Params:
        removee: the User object that will be removed from the removeres friend list.
        """
        remover_friends_list = self

        # Remove friend from removers friend list
        remover_friends_list.remove_friend(removee)

        # Remove friend from removee friend list
        friend_list = FriendsList.objects.get(user=removee)
        friend_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        """
        Check to see if a friend is already in the users friends list.
        """
        if friend in self.friends.all():
            return True
        return False


class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_user')
    is_active = models.BooleanField(blank=False, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

    def accept(self):
        """
        Accept a friend request.
        Update both SENDER and RECEIVER friend lists.
        """
        to_friend_list = FriendsList.objects.get(user=self.to_user)
        if to_friend_list:
            to_friend_list.add_friend(self.from_user)
            sender_friend_list = FriendsList.objects.get(user=self.from_user)
            if sender_friend_list:
                sender_friend_list.add_friend(self.to_user)
                self.is_active = False

    def decline(self):
        """Decline a friend request"""
        self.is_active = False

    def cancel(self):
        """
        Cancel a friend request.
        Is it "cancelled" by setting the `is_active` field to False.
        This is only different with respect to "declining" through the notification that is generated.
        """
        self.is_active = False
        self.save()
