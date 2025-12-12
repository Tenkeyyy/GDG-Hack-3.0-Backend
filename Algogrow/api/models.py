from django.contrib.auth.models import AbstractUser
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.FloatField()
    is_accomplished = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Level(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="levels",
        null=True,
        blank=True,
    )

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    targeted_stat = models.JSONField()
    description = models.TextField()
    difficulty = models.CharField(max_length=6)
    is_accomplished = models.BooleanField(default=False)
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="exercises",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.name
    def diff(self):
        return self.difficulty
class User(AbstractUser):
    email = models.EmailField(blank=False , unique=True)
    age = models.PositiveIntegerField()
    stats = models.JSONField()
    progress = models.JSONField()
    friends = models.ManyToManyField("self",symmetrical=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.username