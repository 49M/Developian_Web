import datetime
from django.shortcuts import render, redirect

from .models import Goal, Reflection
from .forms import GoalForm, ReflectionForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
import random

# Create your views here.
def index(request):
    """The home page for Developian."""
    quotes_file_path = 'developian/static/developian/quotes.txt'
    with open(quotes_file_path, 'r') as file:
        quotes = file.readlines()
        quote = random.choice(quotes).strip()
    content = {'quote': quote}
    return render(request, 'developian/index.html', content)


@login_required
def goals(request):
    """
    Page displaying user goals.
    """
    goals = Goal.objects.filter(owner=request.user).order_by('date_added')
    context = {'goals': goals}
    return render(request, 'developian/goals.html', context)


@login_required
def goal(request, goal_id):
    """
    Show a goal with all its associated reflections.
    """
    goal = Goal.objects.get(id=goal_id)
    # Make sure topic belongs to the logged in user
    # if goal.owner != request.user:
    #     raise Http404
    check_goal_owner(request, goal)
    reflections = goal.reflection_set.order_by('-date_added')
    context = {'goal': goal, 'reflections': reflections}
    return render(request, 'developian/goal.html', context)


@login_required
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
            new_goal = form.save(commit=False)
            new_goal.owner = request.user
            print(f"Saving goal with owner: {new_goal.owner}")
            new_goal.save()
            return redirect('developian:goals')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'developian/new_goal.html', context)


@login_required
def new_reflection(request, goal_id):
    """
    Add a new reflection for a particular goal.
    """
    goal = Goal.objects.get(id=goal_id)
    check_goal_owner(request, goal)

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


@login_required
def edit_reflection(request, reflection_id):
    """
    Edit a previously made reflection.
    """
    reflection = Reflection.objects.get(id=reflection_id)
    goal = reflection.goal
    # if goal.owner != request.user:
    #     raise Http404
    check_goal_owner(request, goal)

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


def check_goal_owner(request, goal):
    """
    Checks if the logged in user matches the user assossiated with the goal.
    """
    if goal.owner != request.user:
        raise Http404

@login_required
def delete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal.delete()
    return redirect('developian:goals')

@login_required
def delete_reflection(request, reflection_id):
    reflection = Reflection.objects.get(id=reflection_id)
    goal = reflection.goal
    check_goal_owner(request, goal)
    reflection.delete()
    return redirect('developian:goal', goal_id=goal.id)

def about(request):
    """
    The About Developian page.
    """
    return render(request, 'developian/about.html')

@login_required
def schedule(request):
    """
    Scheduling page.
    """
    date = datetime.date.today()
    times = ["12:00 am", "1:00 am", "2:00 am", "3:00 am", "4:00 am", "5:00 am", "6:00 am", "7:00 am", "8:00 am", "9:00 am", "10:00 am", "11:00 am", "12:00 pm", "1:00 pm", "2:00 pm", "3:00 pm", "4:00 pm", "5:00 pm", "6:00 pm", "7:00 pm", "8:00 pm", "9:00 pm", "10:00 pm", "11:00 pm"]
    context = {'date': date, 'times': times}
    return render(request, 'developian/schedule.html', context)