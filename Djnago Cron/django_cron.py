# cron.py in_app_folder

...................... django_cron  ........................................
******* Warning: It have to run manually
from django_cron import CronJobBase, Schedule
from .models import ModelName

class ProcessAutomatedTask(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'myapp.Process_Automated_Task'  # Unique identifier
    def do(self):
        pending_keywords = ModelName.objects.filter(status='Pending')
        for task in pending_task:
            
            # Process the keyword here using AI API or any other task
            # Update the keyword status to indicate the completion
            
            task.status = 'Completed'
            task.save()



