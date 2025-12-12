from rest_framework import generics
from .serializers import RegisterSerializer, TraitsSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
class UserStatsView(generics.RetrieveAPIView):
    serializer_class = TraitsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
class UpdateProgressView(generics.UpdateAPIView):
    serializer_class = TraitsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 
def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')