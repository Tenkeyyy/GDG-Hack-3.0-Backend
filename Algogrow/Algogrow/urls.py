from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("" , include("api.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair_view'),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('get_stats', views.get_stats),
]
