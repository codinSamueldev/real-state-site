from django.urls import path

from .views import properties_listing

urlpatterns = [
    path('', properties_listing, name="listing"),
]

