from django.shortcuts import render, redirect

from .models import Goal
from .forms import GoalForm

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

def new_goal(request):
    """
    Add a new goal for the user.
    """
    if request.method != 'POST':
        # No data submitted; creat a blank form.
        form = GoalForm()
    else:
        # POST data submitted; process data.
        form = GoalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('developian:goals')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'developian/new_goal.html', context)