from django.shortcuts import render

# Create your views here.
from rest_framework import generics
# Import the custom User model
from .models import User
# Import the Serializer you just created
from .serializers import UserSignupSerializer

class UserSignupAPIView(generics.CreateAPIView):
    """
    API view for user registration (Signup).
    Handles POST requests to create a new User instance using the UserSignupSerializer.
    """
    # Define the queryset (all User objects) - needed by CreateAPIView
    queryset = User.objects.all()
    
    # Specify which serializer class to use for validating and saving the data
    serializer_class = UserSignupSerializer
    
    # We do not need a permission class, as unauthenticated users must be able to sign up.
