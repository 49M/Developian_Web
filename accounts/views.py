from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from .models import Registration
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required

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
    
@login_required
def account(request):
    """
    Display User account information.
    """
    user = request.user
    username = user.username
    email = user.email
    context = {'username': username, 'email': email}
    return render(request, 'account.html', context)
