from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FriendRequest, FriendsList
from .serializers import FriendRequestSerializer, FriendsListSerializer


class FriendsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a users friend list
        """
        friends_list = FriendsList.objects.filter(user=request.user)
        serializer = FriendsListSerializer(friends_list, many=True)
        return Response(serializer.data)


class FriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Returns a list of Friend Request objects that the requesting user sent
        """
        friend_requests = FriendRequest.objects.filter(from_user=request.user)
        serializer = FriendRequestSerializer(friend_requests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass
