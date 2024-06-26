"""Defines URL patterns for accounts."""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Include default auth URL's
    path('', include('django.contrib.auth.urls')),
]