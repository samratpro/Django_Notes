from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid password or username')
            return redirect('login')
    else:
        template = 'login.html'
        return render(request, template)
    

def logout(request):
    auth.logout(request)
    return redirect('home')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username has already taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,"This email has already taken")
                return redirect('register')
                
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.info(request, 'Successfully created account')
                return redirect('login')
        else:
            messages.info(request, "Password dosen't match")
            return redirect('register')
    else:
        template = 'register.html'
        return render(request, template)
