from django.shortcuts import render

from .models import Goal

# Create your views here.
def index(request):
    """The home page for Developian."""
    return render(request, 'developian/index.html')

def goals(request):
    """
    Page displaying user goals.
    """
    goals = Goal.objects.order_by('date_added')
    context = {'goals': goals}
    return render(request, 'developian/goals.html', context)

def goal(request, goal_id):
    """
    Show a goal with all its associated reflections.
    """
    goal = Goal.objects.get(id=goal_id)
    reflections = goal.reflection_set.order_by('-date_added')
    context = {'goal': goal, 'reflections': reflections}
    return render(request, 'developian/goal.html', context)
