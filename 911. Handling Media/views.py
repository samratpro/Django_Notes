from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Logo

# Create your views here.

@login_required(login_url='login/')
def dashboard(request):
    logos = Logo.objects.first()
    template = 'dashboard/dashboard.html'
    
    context = {'logos':logos}
    return render(request, template, context)
