from django.urls import path, include , re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("api.urls")),
    re_path('login', views.login),
    re_path('signup', views.signup),
    path('send_friend_request/<int:pk>/', views.send_friend_request , name="send-friend-request"),
    path('accept_friend_request/<int:pk>/', views.accept_friend_request, name="accept-friend-request"),
    path('decline_friend_request/<int:pk>/', views.decline_friend_request, name="decline-friend-request"),
    path('my_friends/', views.my_friends, name="my_friends"),
    path('friend_requests/', views.pending_friend_requests),
]
