from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Inherits from Django User base model.
    is_realtor = models.BooleanField(default=False) # For default, users would be home-buyers.
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class RealtorProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user_profile.user.username} - {self.agency_name}"

