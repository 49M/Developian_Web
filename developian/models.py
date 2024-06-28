from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    """A goal the user wants to work towards and accomplish."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return self.text
    
class Reflection(models.Model):
    """Daily goal reflection comment."""
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    reflection = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.reflection[:50]}..."