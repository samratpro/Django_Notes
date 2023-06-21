# General Query All Data
from .models import *
def DataShow(request):
    all_data = WesiteModel.objects.all()
    template = 'data__show__temp__.html'
    context = {'all_data':all_data}
    return render(request, template, context=context)

