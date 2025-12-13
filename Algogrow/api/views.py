from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import Course , User , Exercise , Level , Badge , Friendship
from .serializers import CourseSerializer , UserSerializer , ExerciseSerializer , LevelSerializer , BadgeSerializer , FriendshipSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import math


def growth(x,y):
    return (arctan(x*y)*ln(y))*(arctan(x*y)*ln(y))


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email = request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail" : "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token , created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def pending_friend_requests(request):
    pending = request.user.friendships_received.filter(is_accepted=False)
    serializer = FriendshipSerializer(pending , many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_friends(request):
    friends = request.user.friends.all()
    serializer = UserSerializer(friends, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_friend_request(request,pk):
    try: 
        to_user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({"error" : "User not found"} , status=status.HTTP_404_NOT_FOUND)
    if to_user == request.user:
        return Response({"error" : "You can not send a friend request to yourself"}, status=status.HTTP_400_BAD_REQUEST)
    if Friendship.objects.filter(from_user=request.user , to_user=to_user).exists():
        return Response({"error" : "The friend request has been already sent"}, status=status.HTTP_400_BAD_REQUEST)
    friendship = Friendship.objects.create(from_user=request.user , to_user=to_user)
    serializer = FriendshipSerializer(friendship)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['PATCH'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def accept_friend_request(request, pk):
    try:
        friendship = Friendship.objects.get(id=pk, to_user=request.user, is_accepted=False)
    except Friendship.DoesNotExist:
        return Response({"error": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)
    added = friendship.to_user
    friendship.delete()
    request.user.friends.add(added)
    added.friends.add(request.user)
    return Response({"success" :"Friend has been added successfuly !"} , status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def decline_friend_request(request, pk):
    try:
        friendship = Friendship.objects.get(id=pk, to_user=request.user, is_accepted=False)
    except Friendship.DoesNotExist:
        return Response({"error": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)

    friendship.delete()
    return Response({"message": "Friend request declined"}, status=status.HTTP_204_NO_CONTENT)


class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def delete(self , request , *args , **kwargs):
        Course.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class BadgeListCreate(generics.ListCreateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    def delete(self , request , *args , **kwargs):
        Badge.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def delete(self , request , *args , **kwargs):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class LevelListCreate(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    def delete(self , request , *args , **kwargs):
        Level.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExerciseListCreate(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    def delete(self , request , *args , **kwargs):
        Exercise.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

class CourseDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"
class LevelDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    lookup_field = "pk"
class BadgeDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    lookup_field = "pk"
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    
class CourseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"
class LevelUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    lookup_field = "pk"
class BadgeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    lookup_field = "pk"