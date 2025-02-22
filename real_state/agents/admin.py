from django.contrib import admin
from .models import UserProfile, RealtorProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'is_realtor')
    list_filter = ('is_realtor',)
    search_fields = ('user__username', 'user__email', 'phone_number')

@admin.register(RealtorProfile)
class RealtorProfileAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'agency_name', 'license_number', 'verified')
    list_filter = ('verified', 'agency_name')
    search_fields = ('agency_name', 'license_number')

