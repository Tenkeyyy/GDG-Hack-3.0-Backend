from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    difficulty = models.FloatField()
    level = models.FloatField()
    is_accomplished = models.BooleanField()

    def __str__(self):
        return self.title
