from rest_framework import serializers
# --- FIX: Removed 'Product' from the import as it lives in the 'products' app ---
from .models import User 
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserPublicSerializer(serializers.ModelSerializer):
    """
    Serializer used to safely display the user's profile data (excluding password).
    """
    class Meta:
        model = User
      
        fields = (
            'id', 
            'username', 
            'email', 
            'interest', 
            'dob', 
            'first_name', 
            'last_name', 
            'phone_number'
        )


class UserSignupSerializer(serializers.ModelSerializer):
    """
    Serializer for handling user registration data.
    Ensures the password is hashed before saving.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id', 
            'username', 
            'email', 
            'password', 
            'interest', 
            'dob', 
            'first_name', 
            'last_name', 
            'phone_number'
        )
        read_only_fields = ('id',) 

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user

# --- Updated: Custom JWT Serializer for Login ---

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizes the JWT response to include the full user profile data 
    alongside the access and refresh tokens.
    """
    @classmethod
    def get_token(cls, user):
        # 1. Custom claims (data inside the token payload) remain the same
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['interest'] = user.interest
        return token
    
    def validate(self, attrs):
        # 2. Call the parent validate method, which handles authentication 
        #    and returns the tokens in a dictionary: {'refresh': '...', 'access': '...'}
        data = super().validate(attrs)

        # 3. Retrieve the authenticated user object. The parent class sets self.user.
        user = self.user 

        # 4. Use the new UserPublicSerializer to serialize the user's profile data
        user_data_serializer = UserPublicSerializer(user)

        # 5. Add the serialized user data to the final response dictionary
        data['user'] = user_data_serializer.data

        # The final response body will now include a 'user' object: 
        # {'refresh': '...', 'access': '...', 'user': {...}}
        return data
