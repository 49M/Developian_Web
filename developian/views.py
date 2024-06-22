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
