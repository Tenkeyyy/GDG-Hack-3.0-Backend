from django.contrib.auth.models import AbstractUser
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.FloatField()
    level = models.PositiveIntegerField()
    is_accomplished = models.BooleanField()
    def __str__(self):
        return self.title

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    targeted_stat = models.JSONField()
    description = models.TextField()
    difficulty = models.CharField(max_length=6)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def diff(self):
        return self.difficulty
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=False)
    age = models.PositiveIntegerField()
    stats = models.JSONField()
    progress = models.JSONField()
    def __str__(self):
        return self.username