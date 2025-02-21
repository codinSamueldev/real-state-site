from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import UserProfile, RealtorProfile

from phonenumber_field.formfields import SplitPhoneNumberField

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True, min_length=2)
    email = forms.EmailField(required=True)
    phone_number = SplitPhoneNumberField()
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
        """ 
        The decorator is used to perform a consistent data storage.
        This way if something goes wrong in the middle the user will not be created.
        Enhancing data consistency thorough all DB.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        user.phone_number = self.cleaned_data['phone_number']
        user.address = self.cleaned_data['address']

        if commit:
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            user_profile.save()
            
        return user

class RealtorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = SplitPhoneNumberField()
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    agency_name = forms.CharField(max_length=100, required=True)
    license_number = forms.CharField(max_length=50, required=True)
    years_of_experience = forms.IntegerField(min_value=0, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
    
    def clean_license_number(self):
        license_number = self.cleaned_data.get('license_number')
        if RealtorProfile.objects.filter(license_number=license_number).exists():
            raise ValidationError("A realtor with this license number already exists.")
        return license_number
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create UserProfile first
            user_profile = UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address'],
                is_realtor=True
            )
            
            # Now create RealtorProfile
            realtor_profile = RealtorProfile.objects.create(
                user_profile=user_profile,
                agency_name=self.cleaned_data['agency_name'],
                license_number=self.cleaned_data['license_number'],
                years_of_experience=self.cleaned_data['years_of_experience']
            )
        
        return user