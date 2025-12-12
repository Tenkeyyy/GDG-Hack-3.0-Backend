from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.response import Response
from .models import Course , User , Exercise
from .serializers import CourseSerializer , UserSerializer , ExerciseSerializer
from rest_framework.generics import DestroyAPIView


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
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    
class CourseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "pk"