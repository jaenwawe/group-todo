from django.urls import path
from .views import FriendsListView, FriendRequestView

urlpatterns = [
    path('friend-list', FriendsListView.as_view()),
    path('friend-requests', FriendRequestView.as_view()),
]
