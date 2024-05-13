from django.db import models

# Create your models here.
class Goal(models.Model):
    """A goal the user wants to work towards and accomplish."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Returns a string representation of the model."""
        return self.text