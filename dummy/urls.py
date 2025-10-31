
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('api/v1/accounts/', include('accounts.urls')), 
 
]
