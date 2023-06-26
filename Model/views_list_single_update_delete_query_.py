# General Query All Data
from .models import *

"""
``` All Document: https://github.com/samratpro/Django-Component/blob/master/Model/queryset.md ```
    MyModel.objects.all()                  ``` Get All data
    MyModel.objects.filter(field=value)    ``` Filter return **List/multiple data**, It can be used for any backend continuous logic until getting certain data
    MyModel.objects.get(field=value)       ``` Get return **Single Data**, 
    
``` Here filed list: ```
    Document: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#id4
    pk = Primary Key
    id = Identity Like PK
    custom_name = Our created custom variable name
    custom_name__contains = custom_name is variable
    id__in= [1, 3, 4] *** it can take multiple or Single id values
    custom_name__in =  *** It can take multiple or Single id values       
    
``` Render data from the Model don't affect your POST or GET method Runtime, ```
``` VT(view.py to temple.html) data will affect by the User action, ```
``` MTV(Models Views Template) data won't affect by the User action ..without Logic.., ```
"""

# Save data .....................................
def website(request):
    template = 'add_data_.html'
    if request.method == 'POST':
        form = DataForms(request.POST)
        context = {'data_form':form}
        if form.is_valid():
            data_name = form.cleaned_data['data_name']
            data_url = form.cleaned_data['data_url']
            obj = DataModel(data_name=data_name, data_url=data_url)
            obj.save()
            return redirect('/alldata')
        else:
            return redirect('/add_data')
    else:
        form = DataForms()
        context = {'data_form':form}
        return render(request, template, context=context)

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
            return redirect('/alldata')
    else:
        update_form = WebsiteForms(initial={
            'data_name': website.data_name,
            'data_url': website.data_url,
        })
    context = {'update_form': update_form,'data_id': data_id}
    return render(request, template, context)

# Delete Data ...................................................
def delete_data(request, data_id):
    data = WesiteModel.objects.get(pk=data_id)
    data.delete()
    return redirect('/alldata')


# Select Data From different Model From HTML Template
def MakingPost(request):
    template = 'Data_From_different_Model.html'
    website = WesiteModel.objects.all()
    api = OpenaiAPIModel.objects.all()
    context = {'api':api, 'website':website}
    
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        
        website_id = request.POST['website_id']
        targeted_website = WesiteModel.objects.get(pk=website_id)

        api_id = request.POST['api_id']
        targeted_api = OpenaiAPIModel.objects.get(pk=api_id)

        # Do action with these data, also look how html file working
        
        return redirect('makingpost')
    
    return render(request, template, context=context)

