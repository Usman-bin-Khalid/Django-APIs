from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# comments/views.py
from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
# Assuming you want the same permission: only the comment owner can edit/delete
from products.permissions import IsOwnerOrReadOnly 


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed, created, updated, or deleted.
    
    - Only authenticated users can view, create, update, or delete.
    - Owners can update/delete their own comments (using IsOwnerOrReadOnly, where owner is 'commenter').
    """
    # Get all comments
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer
    
    # Only authenticated users can interact
    # We will reuse IsOwnerOrReadOnly, but it will check the 'commenter' field.
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        """
        When creating a new comment, automatically set the 'commenter' field
        to the currently logged-in user (request.user).
        """
        # Save the serializer data, setting the commenter before commit
        # The IsOwnerOrReadOnly class should be updated to check the 'commenter' field 
        # instead of 'owner' if you are reusing it directly.
        # Alternatively, ensure IsOwnerOrReadOnly checks obj.commenter == request.user 
        # for a Comment instance.
        serializer.save(commenter=self.request.user)