from django import forms

from .models import Goal, Reflection

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['text']
        labels = {'text': ''}

class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = ['reflection']
        labels = {'reflection': ''}
        widgets = {'reflection': forms.Textarea(attrs={'cols': 80})}

