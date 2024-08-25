"""Defines URL patterns for accounts."""

from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView


from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth URL's
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Password change views
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # Registration page
    path('register/', views.register, name='register'),
    # Verify user
    path('verify/<str:token>', views.verify, name='verify'),
    # Account page
    path('info', views.account, name='info'),
]