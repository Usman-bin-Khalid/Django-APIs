from django.db import models

# Create your models here.
from django.db import models
# Import settings to reference the custom User model safely
from django.conf import settings 

class Product(models.Model):
    """
    Model to store product details, linked to the user who created it (the owner).
    """
    # Links the product to the user who created it (ForeignKey)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Product Owner"
    )
    
    # Core Product Fields
    Productname = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField(default=1)
    # Use DecimalField for financial accuracy
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    # Image field (requires 'Pillow' library installed: pip install Pillow)
    prodImg = models.ImageField(
        upload_to='product_images/', 
        blank=True, 
        null=True,
        help_text="Product image file."
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # Order products by name by default
        ordering = ['Productname'] 

    def __str__(self):
        return f"{self.Productname} (Owned by {self.owner.username})"
