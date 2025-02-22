from django.contrib import admin

from .models import Properties

# Register your models here.

@admin.register(Properties)
class Properties(admin.ModelAdmin):
    list_display = ('title', 'location', 'property_type', 'price', 'pub_date')
    list_filter = ('property_type',)
    search_fields = ('title', 'location', 'pub_date')

