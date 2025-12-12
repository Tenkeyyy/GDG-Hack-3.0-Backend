from django.urls import path
from .views import RegisterView, UserStatsView, UpdateProgressView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("stats/", UserStatsView.as_view(), name="stats"),
    path("progress/update/", UpdateProgressView.as_view(), name="update-progress"),
]
