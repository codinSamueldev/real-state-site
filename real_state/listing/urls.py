from django.urls import path

from .views import properties_listing, add_listing

urlpatterns = [
    path('', properties_listing, name="listing"),
    path('add-listing/', add_listing, name="add-listing"),
]

