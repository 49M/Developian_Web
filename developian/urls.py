"""Defines URL patterns for developian"""

from django.urls import path

from . import views

app_name = 'developian'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Goal Page
    path('goals/', views.goals, name='goals'),
    # Individual Goal Page
    path('goals/<int:goal_id>/', views.goal, name='goal'),
    # Page for adding new goals
    path('new_goal/', views.new_goal, name='new_goal'),
]