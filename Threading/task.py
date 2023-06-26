from .models import *
from time import sleep

def BulkDataJob():
    pending_datas = BulkDataModel.objects.filter(status='Pending')
    for data in pending_datas:
        sleep(10)
        data.content = 'Content'
        data.status = 'Completed'
        data.save()
