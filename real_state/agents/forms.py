from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import UserProfile, RealtorProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_email(self):
        """
        Make sure each User whether is a home-buyer or Realtor has a unique Email address.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            user_profile = UserProfile.objects.get(user=user)
            user_profile.phone_number = self.cleaned_data['phone_number']
            user_profile.address = self.cleaned_data['address']
            user_profile.save()
            
        return user

class RealtorRegistrationForm(UserRegistrationForm):
    agency_name = forms.CharField(max_length=100, required=True)
    license_number = forms.CharField(max_length=50, required=True)
    years_of_experience = forms.IntegerField(min_value=0, required=True)
    
    def clean_license_number(self):
        """
        Make sure each Realtor has a unique license number in the platform.
        This is done to ensure an extra layer of security for home-buyers in decision making.
        """
        license_number = self.cleaned_data.get('license_number')
        if RealtorProfile.objects.filter(license_number=license_number).exists():
            raise ValidationError("A realtor with this license number already exists.")
        return license_number
    
    @transaction.atomic
    def save(self, commit=True):
        """ 
        The decorator is used to perform a consistent data storage.
        This way if something goes wrong in the middle the user will not be created.
        Enhancing data consistency thorough all DB.
        """
        user = super().save(commit=False)
        
        if commit:
            user.save()
            user_profile = UserProfile.objects.get(user=user)
            user_profile.is_realtor = True
            user_profile.save()
            
            realtor_profile = RealtorProfile.objects.create(
                user_profile=user_profile,
                agency_name=self.cleaned_data['agency_name'],
                license_number=self.cleaned_data['license_number'],
                years_of_experience=self.cleaned_data['years_of_experience']
            )
            
        return user

