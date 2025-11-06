# comments/serializers.py
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    # Read-only fields to display user-friendly names instead of IDs
    commenter_username = serializers.ReadOnlyField(source='commenter.username')
    product_name = serializers.ReadOnlyField(source='product.Productname')
    
    class Meta:
        model = Comment
        fields = [
            'id', 
            'product',           # ID of the product being commented on (needed for POST)
            'product_name',      # Read-only product name for display
            'commenter',         # ID of the commenter (will be set automatically)
            'commenter_username', # Read-only commenter username for display
            'content',           # The comment text
            'created_at'         # Read-only timestamp
        ]
        # Prevent client from setting 'commenter' and 'created_at' directly
        read_only_fields = ['commenter', 'created_at']