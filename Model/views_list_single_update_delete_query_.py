# General Query All Data
from .models import *

# Showing all data, like post .....................................................
def AllDataShow(request):
    all_data = WesiteModel.objects.all()
    template = 'all_data_show.html'
    context = {'all_data':all_data}
    return render(request, template, context=context)

# Viewing Single Data .....................................
def single_data(request, data_id):
    template = "single_data.html"
    sigle_data = WesiteModel.objects.get(pk=data_id)
    context = {'sigle_data': sigle_data,'data_id': data_id}
    return render(request, template, context)  



# Update Data ...................................................
def update_data(request, data_id):
    template = "update_data.html"
    data = WesiteModel.objects.get(pk=data_id)
    if request.method == "POST":
        update_form = WebsiteForms(request.POST)
        if update_form.is_valid():
            data.data_name = update_form.cleaned_data['data_name']
            data.data_url = update_form.cleaned_data['data_url']
            data.save()
            return redirect('/website')
    else:
        update_form = WebsiteForms(initial={
            'data_name': website.data_name,
            'data_url': website.data_url,
        })
    context = {'update_form': update_form,'data_id': data_id}
    return render(request, template, context)

