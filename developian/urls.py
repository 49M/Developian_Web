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
     # Page for adding reflections under goals
     path('new_reflection/<int:goal_id>/', views.new_reflection, 
          name='new_reflection'),
     # Page for editing reflections
     path('edit_reflection/<int:reflection_id>/', views.edit_reflection, 
          name='edit_reflection'),
     # Page for deleting goals
     path('delete_goal/<int:goal_id>/', views.delete_goal, 
          name='delete_goal'),
     # Delete reflections
     path('delete_reflection/<int:reflection_id>/', views.delete_reflection,
          name='delete_reflection'),
     path('about/', views.about, name='about'),
     # Scheduling Page
     path('schedule/', views.schedule, name='schedule'),
]