from django.db import models

class Course(models.Model):
    title = models.TextField(unique=True)
    description = models.TextField()
    difficulty = models.IntegerField()
    level = models.FloatField()
    is_accomplished = models.BooleanField()

    def __str__(self):
        return self.title
