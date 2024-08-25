# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from .models import Registration
# from .forms import RegistrationForm
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
# from django.conf import settings
# from django.http import HttpResponse
# import random

# def register(request):
#     """
#     Register a new user.
#     """
#     if request.method != 'POST':
#         # Display blank registration form
#         form = UserCreationForm()
#     else:
#         # Process completed form.
#         # form = UserCreationForm(data=request.POST)
#         form = RegistrationForm(data=request.POST)

#         if form.is_valid():
#             new_user = form.save()
#             # Log in the user and redirect to home page
#             login(request, new_user)
#             return redirect('developian:index')
#     # Display blank or invalid form
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

# def register(request):
#     """
#     Register a new user.
#     """
#     form = RegistrationForm()
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = Registration(email=email, username=username, password=password)
#         domain_name = get_current_site(request).domain
#         token = str(random.random()).split('.')[1]
#         user.token = token

#         link = f'http://{domain_name}/accounts/verify/{token}'

#         send_mail('Verify Email', 
#                   f'Please click the link below to verify your account email.\n{link}', 
#                   settings.EMAIL_HOST_USER, [email], fail_silently=False)
#         return HttpResponse('Email verification has been sent!')

#         # return redirect('developian:index')
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

# def verify(request, token):
#     try:
#         user = Registration().objects.filter(token=token)
#         if user:
#             user.is_verified = True
#         return redirect('developian:index')
#     except Exception as e:
#         print(e)
#         form = RegistrationForm()
#         context = {'form': form}
#         return render(request, 'registration/register.html', context)


# views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from .models import Registration
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random

def register(request):
    """
    Register a new user.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = Registration(email=email, username=username)
            user.set_password(password)  # Hash the password
            token = str(random.random()).split('.')[1]
            user.token = token
            user.save()

            domain_name = get_current_site(request).domain
            link = f'http://{domain_name}/accounts/verify/{token}'

            send_mail(
                'Verify Email',
                f'Please click the link below to verify your account email.\n{link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            return HttpResponse('Email verification has been sent!')

    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


# views.py

def verify(request, token):
    try:
        user = get_object_or_404(Registration, token=token)
        user.is_verified = True
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Log the user in
        return redirect('developian:index')
    except Exception as e:
        print(e)
        return HttpResponse('Verification failed. Please try again.')
