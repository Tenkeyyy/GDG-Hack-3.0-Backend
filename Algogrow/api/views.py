from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import Course , User , Exercise , Level
from .serializers import CourseSerializer , UserSerializer , ExerciseSerializer , LevelSerializer
from rest_framework.generics import DestroyAPIView
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username = request.data['username'])
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
def get_stats(request):
    return Response(request.user.password)
class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def delete(self , request , *args , **kwargs):
        Course.objects.all().delete()
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