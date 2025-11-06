from django.db import models

# Create your models here.
# comments/models.py
from django.db import models
from django.conf import settings
# Import the Product model from the 'product' app
from products.models import Product 

class Comment(models.Model):
    """
    Model to store comments on specific products.
    """
    # The user who posted the comment (ForeignKey to the custom User model)
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Commenter"
    )
    
    # The product the comment is on (ForeignKey to the Product model)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Product Commented On"
    )
    
    # The content of the comment
    content = models.TextField()
    
    # Timestamp for when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        # Order comments by the newest first
        ordering = ['-created_at'] 

    def __str__(self):
        # Display a snippet of the comment and the product name
        return f"Comment by {self.commenter.username} on {self.product.Productname}: \"{self.content[:30]}...\""