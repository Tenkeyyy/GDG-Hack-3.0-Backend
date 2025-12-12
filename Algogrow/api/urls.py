from django.urls import path
from . import views

urlpatterns = [
    path("Course/", views.CourseListCreate.as_view(), name="Course-view-create"),
    path("Exercise/", views.ExerciseListCreate.as_view(), name="exercise-view-create"),
    path("User/", views.UserListCreate.as_view(), name="user-view-create"),
    path("Level/", views.LevelListCreate.as_view(), name="level-view-create"),
    path("User/Delete/<int:pk>/", views.UserDeleteView.as_view(), name="user-delete-view"),
    path("Course/Delete/<int:pk>/", views.CourseDeleteView.as_view(), name="course-delete-view"),
    path("Level/Delete/<int:pk>/", views.LevelDeleteView.as_view(), name="level-delete-view"),
    path("User/Update/<int:pk>/", views.UserUpdateView.as_view(), name="user-Update-view"),
    path("Course/Update/<int:pk>/", views.CourseUpdateView.as_view(), name="course-Update-view"),
    path("Level/Update/<int:pk>/", views.LevelUpdateView.as_view(), name="level-Update-view"),
]
