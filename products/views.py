from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer
# --- CHANGE: Import IsOwnerOrReadOnly from its dedicated file ---
from .permissions import IsOwnerOrReadOnly # This assumes products/permissions.py is present


# --- NOTE: The IsOwnerOrReadOnly class is removed from here ---


# --- Product ViewSet (Handles all CRUD operations) ---

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed, created, updated, or deleted.
    It automatically handles URL routing for list/create and retrieve/update/delete.
    """
    # Queryset for all products
    queryset = Product.objects.all().order_by('id') 
    serializer_class = ProductSerializer
    
    # Applying the permission classes:
    # 1. IsAuthenticated: Ensures user is logged in (has a valid JWT).
    # 2. IsOwnerOrReadOnly: Implements the 'view all, edit/delete own' logic.
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        When creating a new product via POST, automatically set the 'owner' field
        to the currently logged-in user (request.user).
        """
        # Save the serializer data, setting the owner before commit
        serializer.save(owner=self.request.user)
