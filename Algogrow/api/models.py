from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.FloatField()
    is_accomplished = models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Level(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True , null=True)
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
    age = models.PositiveIntegerField(blank=True, null=True)
    stats = models.JSONField(null=True , blank=True)
    progress = models.JSONField(blank=True , null=True)
    friends = models.ManyToManyField("self",symmetrical=True, blank=True)
    REQUIRED_FIELDS = [ 'email' , 'age']
    def __str__(self):
        return self.username
class Badge(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="badges",
        null=True,
        blank=True,
    )
class Friendship(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="friendships_sent",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="friendships_received",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate requests between the same two users
        unique_together = ("from_user", "to_user")

    def __str__(self):
        status = "accepted" if self.is_accepted else "pending"
        return f"{self.from_user} → {self.to_user} ({status})"
