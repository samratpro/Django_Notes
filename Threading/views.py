from .task import *
import threading


scheduler_thread = None  
def bulkpost(request):
    template = 'bulkpost.html'
    keyword_pending = BulkKeywordModel.objects.filter(status='Pending')
    context = {'keyword_pending': keyword_pending}

    if request.method == 'POST':
        keyword_list = request.POST.get('keyword_list')
        keywords = keyword_list.split('\n')

        for keyword in keywords:
            keyword = keyword.strip()
            if keyword:
                BulkKeywordModel.objects.create(name=keyword, status='Pending')

        global scheduler_thread
        if scheduler_thread is None or not scheduler_thread.is_alive():
            # Start the task scheduler in a separate thread
            scheduler_thread = threading.Thread(target=BulkDatasJob)      #  We can also input BulkDatasJob function's argument
            # scheduler_thread = threading.Thread(target=BulkDatasJob, args=('arg',)) 
            scheduler_thread.start()
        return redirect('bulkpost')
    
    return render(request, template, context=context)
