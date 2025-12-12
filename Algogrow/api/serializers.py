from rest_framework import serializers
from .models import Course , Exercise , User , Level


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id" , "title" , "description" , "difficulty" , "is_accomplished" , "levels"]
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise 
        fields = ["id" ,"name" , "targeted_stat" , "description" , "difficulty" , "is_accomplished" ]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "email" , "age" , "stats" , "progress"]
class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level 
        fields = ["id" , "title" , "course" , "exercises"]