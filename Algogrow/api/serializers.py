from rest_framework import serializers
from .models import Course , Exercise , User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id" , "title" , "description" , "difficulty" , "level" , "is_accomplished"]
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise 
        fields = ["id" ,"name" , "targeted_stat" , "description" , "difficulty" , "is_done" ]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "email" , "age" , "stats" , "progress"]