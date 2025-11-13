# comments/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
# Register the CommentViewSet
router.register(r'comments', CommentViewSet, basename='comment') 

# The API URLs are now determined automatically by the router:
# /comments/ (GET: list, POST: create)
# /comments/{id}/ (GET: retrieve, PUT/PATCH: update, DELETE: destroy)
urlpatterns = [
    path('', include(router.urls)), 
]