from django.shortcuts import render
from django.http import HttpResponse
from .models import InfoBulkModel

def submit_keywords(request):
    if request.method == 'POST':
        keyword_list = request.POST.get('keywords', '').split(',')
        user = request.user  # Replace with your authentication logic

        for keyword in keyword_list:
            InfoBulkModel.objects.create(user=user, keyword=keyword.strip(), status='Pending')

        return HttpResponse("Keywords submitted successfully!")
    else:
        return render(request, 'submit_keywords.html')
