"""Defines URL patterns for accounts."""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth URL's
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
    # Verify user
    path('verify/<str:token>', views.verify, name='verify'),
    # Account page
    path('info', views.account, name='info'),
]