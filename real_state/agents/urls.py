from django.urls import path

from . import views

urlpatterns = [
    path('', views.type_user_redirect, name="redirect_question"),
    path('user/', views.user_registration, name="home-buyer"),
    path('realtor/', views.realtor_registration, name="realtor"),
]

