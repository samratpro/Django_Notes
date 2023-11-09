from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import AppUser, Task, TaskPermission

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Handle invalid login

    return render(request, 'login.html')

def dashboard(request):
    if request.user.is_teacher:
        # Display teacher dashboard
        tasks = Task.objects.filter(assigned_to=request.user)
    elif request.user.is_student:
        # Display student dashboard
        tasks = Task.objects.filter(assigned_to=request.user)
    else:
        # Handle other user types
        tasks = []

    return render(request, 'dashboard.html', {'tasks': tasks})
