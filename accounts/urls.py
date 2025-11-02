from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
# Import our custom views
from .views import UserSignupAPIView, CustomTokenObtainPairView

urlpatterns = [
    # 1. Signup API (existing)
    path('signup/', UserSignupAPIView.as_view(), name='user-signup'),

    # 2. JWT Login/Token Generation API (New)
    # Input: POST request with { "username": "...", "password": "..." }
    # Output: { "refresh": "...", "access": "..." }
    # API path for login
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # 3. JWT Token Refresh API (New)
    # Input: POST request with { "refresh": "..." }
    # Output: { "access": "..." }
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
