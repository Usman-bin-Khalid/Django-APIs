from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer

# --- Custom Permission Class to implement "View All, Edit/Delete Own" logic ---

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object (product) to edit or delete it.
    Read permissions (GET, HEAD, OPTIONS) are allowed for any authenticated user.
    """
    message = 'Editing or deleting is restricted to the owner of this product.'

    def has_object_permission(self, request, view, obj):
        # 1. Allow read permissions for safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # 2. For write methods (PUT, PATCH, DELETE), check if the user is the owner
        # request.user is available because of JWTAuthentication
        return obj.owner == request.user

# --- Product ViewSet (Handles all CRUD operations) ---

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    It uses JWTAuthentication provided by the REST_FRAMEWORK settings.
    """
    # Queryset for all products
    queryset = Product.objects.all().order_by('id') 
    serializer_class = ProductSerializer
    
    # Applying the permission classes:
    # 1. IsAuthenticated: Ensures user is logged in (has a valid JWT).
    # 2. IsOwnerOrReadOnly: Implements the 'view all, edit own' logic.
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        When creating a new product via POST, automatically set the 'owner' field
        to the currently logged-in user (request.user).
        """
        # Save the serializer data, setting the owner before commit
        serializer.save(owner=self.request.user)
