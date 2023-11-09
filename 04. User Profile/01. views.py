@login_required(login_url='login/')
def profile(request):
    template = 'user/profile/profile.html'
    
    context = {}
    return render(request, template, context)
