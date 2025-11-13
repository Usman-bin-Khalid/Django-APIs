from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # This read-only field displays the username of the owner
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = [
            'id', 
            'owner', 
            'owner_username', 
            'Productname', 
            'description', 
            'quantity', 
            'price', 
            'prodImg'
        ]
        # Prevents the 'owner' ID from being set by the client
        read_only_fields = ['owner'] 
