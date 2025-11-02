from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework import permissions # Keep permissions for BasePermission

# Note: Product imports are removed.
from .models import User
from .serializers import UserSignupSerializer, CustomTokenObtainPairSerializer

class UserSignupAPIView(generics.CreateAPIView):
    """
    API view for user registration (Signup).
    """
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view that uses the CustomTokenObtainPairSerializer.
    This handles the authentication (username/password check) and token generation.
    """
    serializer_class = CustomTokenObtainPairSerializer

# The IsOwnerOrReadOnly permission is moved to products/views.py where it is used.
# If you want to keep the definition here, you must change the imports to be absolute:
# from products.models import Product 
