from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product') # Added basename for explicit naming

# The API URLs are now determined automatically by the router:
# /products/ (GET: list, POST: create)
# /products/{id}/ (GET: retrieve, PUT/PATCH: update, DELETE: destroy)
urlpatterns = [
    path('', include(router.urls)), 
]
