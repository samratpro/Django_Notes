# General Query All Data
from .models import *

# Showing all data, like post .....................................................
def AllDataShow(request):
    all_data = WesiteModel.objects.all()
    template = 'all_data_show.html'
    context = {'all_data':all_data}
    return render(request, template, context=context)






# Update Data ...................................................
def update_website(request, website_id):
    template = "update_website.html"
    website = WesiteModel.objects.get(pk=website_id)
    if request.method == "POST":
        update_form = WebsiteForms(request.POST)
        if update_form.is_valid():
            website.website_name = update_form.cleaned_data['website_name']
            website.website_url = update_form.cleaned_data['website_url']
            website.username = update_form.cleaned_data['username']
            website.app_pass = update_form.cleaned_data['app_pass']
            website.save()
            return redirect('/website')
    else:
        update_form = WebsiteForms(initial={
            'website_name': website.website_name,
            'website_url': website.website_url,
            'username': website.username,
            'app_pass': website.app_pass
        })
    context = {'update_form': update_form,'website_id': website_id}
    return render(request, template, context)

