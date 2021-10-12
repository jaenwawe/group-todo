from rest_framework import serializers

from .models import FriendsList, FriendRequest


class FriendsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsList
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'
