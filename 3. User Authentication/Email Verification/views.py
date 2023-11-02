from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AppUser              # Custom User from Model
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.crypto import get_random_string


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')   # ``dashboard`` path is destination
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                next_url = request.GET.get('next')  # `` Get next `` will grab next targeted URL, which page was requested by User that need to Login
                if next_url:
                    return redirect(next_url)
                else:
                   return redirect('dashboard')
            else:
                messages.info(request, 'Invalid password or username')
                return redirect(request.get_full_path()) # When fail to login, need to return current URL cause next URL and normal URL are different
        else:
            template = 'login.html'
            return render(request, template)
    
# Must be follow this function
def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 and password1 == password2:
            if AppUser.objects.filter(username=username).exists():
                messages.info(request,'This username has already taken')
                return redirect('register')
            elif AppUser.objects.filter(email=email):
                messages.info(request,"This email has already taken")
                return redirect('register')
                
            else:
                user = AppUser.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                
                
                activation_code = get_random_string(30)
                user.activation_code = activation_code
                user.save()

                # Send activation email
                current_site = get_current_site(request)
                domain = current_site.domain
                activation_link = f'{domain}/activate/{activation_code}/'
                send_mail(
                    'Activate Your Account',
                    f'Click the following link to activate your account: {activation_link}',
                    'from@example.com',
                    [email],
                    fail_silently=False
                )
                
                messages.info(request, 'Successfully created account')
                return redirect('login')
        else:
            messages.info(request, "Password dosen't match")
            return redirect('register')
    else:
        template = 'register.html'
        return render(request, template)



def activate_account(request, activation_code):
    try:
        user = AppUser.objects.get(activation_code=activation_code, is_active=False)
    except AppUser.DoesNotExist:
        # Handle the case where the activation code is invalid or the account is already active
        return render(request, 'activation_failed.html')

    # Activate the user account
    user.activate()
    return render(request, 'activation_success.html')
