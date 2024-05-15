from django.contrib import admin

# Register your models here.
from .models import Goal, Reflection

admin.site.register(Goal)
admin.site.register(Reflection)