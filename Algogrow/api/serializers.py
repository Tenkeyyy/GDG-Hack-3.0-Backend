from rest_framework import serializers
from .models import Course , Exercise , User , Level , Badge , Friendship


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id" , "title" , "description" , "difficulty" , "is_accomplished" , "levels" ]
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise 
        fields = ["id" ,"name" , "targeted_stat" , "description" , "difficulty" , "is_accomplished" ]
class UserSerializer(serializers.ModelSerializer):
    badges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    friendships_received = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    friendships_sent = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ["id" , "username" , "email" , "age" , "stats" , "progress" , "badges" , "friendships_received" , "friendships_sent"]
class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level 
        fields = ["id" , "title" , "description" , "course" , "exercises"]
class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge 
        fields = ["id" , "title" , "description" , "owner"]
class FriendshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friendship
        fields = ["id" , "from_user" , "to_user" , "is_accepted" , "created_at"]