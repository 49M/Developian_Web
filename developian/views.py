from django.shortcuts import render, redirect

from .models import Goal, Reflection
from .forms import GoalForm, ReflectionForm

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


def new_reflection(request, goal_id):
    """
    Add a new reflection for a particular goal.
    """
    goal = Goal.objects.get(id=goal_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = ReflectionForm()
    else:
        # POST data submitted; process data.
        form = ReflectionForm(data=request.POST)
        if form.is_valid():
            new_reflection = form.save(commit=False)
            new_reflection.goal = goal
            new_reflection.save()
            return redirect('developian:goal', goal_id=goal_id)
        
    # Display blank or invalid form
    context = {'goal': goal, 'form': form}
    return render(request, 'developian/new_reflection.html', context)


def edit_reflection(request, reflection_id):
    """
    Edit a previously made reflection.
    """
    reflection = Reflection.objects.get(id=reflection_id)
    goal = reflection.goal

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = ReflectionForm(instance=reflection)
    else:
        # POST data submitted; process entry
        form = ReflectionForm(instance=reflection, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('developian:goal', goal_id=goal.id)
    
    context = {'reflection': reflection, 'goal': goal, 'form': form}
    return render(request, "developian/edit_reflection.html", context)
