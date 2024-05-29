"""Defines URL patterns for developian"""

from django.urls import path

from . import views

app_name = 'developian'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]