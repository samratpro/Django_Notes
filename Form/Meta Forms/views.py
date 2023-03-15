from django.shortcuts import render
from .forms import *
from .models import *



def contactus(request):

    form = ContactForm(request.POST or None)
    context = {'test_form':form}
    if form.is_valid():
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        context['name'] = name
        context['phone'] = phone
        context['message'] = message
        form.save()

    template = 'contact.html'
    return render(request, template, context=context)