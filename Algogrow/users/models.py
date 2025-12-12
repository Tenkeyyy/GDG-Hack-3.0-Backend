from django.contrib.auth.models import AbstractUser
from django.db import models

def default_traits():
    return {
        "memory": {"score": 0, "recall_speed": 0},
        "speed": {"avg_time": 0, "reaction_time": 0},
        "logic": {"accuracy": 0, "mistakes": 0},
        "problem_solving": {"success_rate": 0, "hints_used": 0},
        "algorithmic_thinking": {"ds_choice_accuracy": 0, "complexity_estimate_accuracy": 0},
        "focus": {"streak": 0, "avg_session_length": 0},
        "motivation": {"badges": [], "extra_practice": 0}
    }

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None   
    traits = models.JSONField(default=default_traits)
    age = models.IntegerField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email