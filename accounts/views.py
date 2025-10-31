from rest_framework import generics
# Import the base view from simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView 
from .models import User
# Import the serializers, including the new custom token serializer
from .serializers import UserSignupSerializer, CustomTokenObtainPairSerializer

# --- Existing Signup View ---

class UserSignupAPIView(generics.CreateAPIView):
    """
    API view for user registration (Signup).
    """
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    
# --- NEW: Custom Login View ---

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view that uses the CustomTokenObtainPairSerializer.
    This handles the authentication (username/password check) and token generation.
    """
    serializer_class = CustomTokenObtainPairSerializer
