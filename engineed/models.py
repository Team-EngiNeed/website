from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return f"Message from {self.full_name}"




class Submission(models.Model):
    # Replace 'User' with 'settings.AUTH_USER_MODEL'
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Dynamically uses the custom user model
        on_delete=models.CASCADE,
        default=None
    )
    fullName = models.CharField(max_length=75)
    gradeSection = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    
    # Changed from auto_now_add to allow manual input of date
    dateSubmitted = models.DateTimeField(null=False, blank=False, default=timezone.now)  # Or any default datetime

    # New fields for the damaged property dropdown, image, and comment
    DAMAGED_PROPERTY_CHOICES = [
        ('chair', 'Chair'),
        ('table', 'Table'),
        ('electricfan', 'Electric Fan'),
        ('outlet', 'Outlet'),
        ('television', 'Television'),
        ('whiteboard', 'Whiteboard'),
        ('tiles', 'Tiles'),
        ('window', 'Window'),
    ]

    # Dropdown menu for damaged property
    damagedProperty = models.CharField(
        max_length=50,
        choices=DAMAGED_PROPERTY_CHOICES,  # Choices for the dropdown
        default='chair'  # You can set a default if needed
    )


    # Comment field
    comment = models.SlugField(null=True, blank=True)  # Optional comment field

    def __str__(self):
        # Return a string with fullName, gradeSection, damagedProperty, and comment (if available)
        return f"{self.fullName} ({self.gradeSection}) - Damaged Property: {self.damagedProperty}, Comment: {self.comment or 'No comment'}"
