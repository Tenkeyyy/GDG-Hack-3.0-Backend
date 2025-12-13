from django.urls import path
from . import views

urlpatterns = [
    path("Course/", views.CourseListCreate.as_view(), name="Course-view-create"),
    path("Exercise/", views.ExerciseListCreate.as_view(), name="exercise-view-create"),
    path("User/", views.UserListCreate.as_view(), name="user-view-create"),
    path("Level/", views.LevelListCreate.as_view(), name="level-view-create"),
    path("Badge/", views.BadgeListCreate.as_view(), name="badge-view-create"),
    path("User/Delete/<int:pk>/", views.UserDeleteView.as_view(), name="user-delete-view"),
    path("Course/Delete/<int:pk>/", views.CourseDeleteView.as_view(), name="course-delete-view"),
    path("Level/Delete/<int:pk>/", views.LevelDeleteView.as_view(), name="level-delete-view"),
    path("Badge/Delete/<int:pk>/", views.BadgeDeleteView.as_view(), name="badge-delete-view"),
    path("User/Update/<int:pk>/", views.UserUpdateView.as_view(), name="user-update-view"),
    path("Course/Update/<int:pk>/", views.CourseUpdateView.as_view(), name="course-update-view"),
    path("Level/Update/<int:pk>/", views.LevelUpdateView.as_view(), name="level-update-view"),
    path("Badge/Update/<int:pk>/", views.BadgeUpdateView.as_view(), name="badge-update-view"),
]
