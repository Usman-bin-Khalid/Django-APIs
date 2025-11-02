from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Built-in fields we inherit: username, email, password, is_active, etc.

    # 1. Custom Field: Interest (CharField)
    interest = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="User's primary area of interest."
    )
    
    # 2. Custom Field: Date of Birth (DateField)
    dob = models.DateField(
        blank=True, 
        null=True, 
        help_text="User's date of birth."
    )
    
    # 3 & 4. Standard name fields (often useful for profiles)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    
    # 5. Additional custom field: Phone Number
    phone_number = models.CharField(
        max_length=20, 
        unique=True, 
        blank=True, 
        null=True, 
        help_text="User's unique phone number."
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
