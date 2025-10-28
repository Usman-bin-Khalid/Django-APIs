from django.urls import path
# Import the view we created in views.py
from .views import UserSignupAPIView

urlpatterns = [
    # This path maps 'signup/' to our UserSignupAPIView.
    # The .as_view() method is used when connecting a class-based view to a URL.
    path('signup/', UserSignupAPIView.as_view(), name='user-signup'),
]
