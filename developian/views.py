from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Developian."""
    return render(request, 'developian/index.html')
