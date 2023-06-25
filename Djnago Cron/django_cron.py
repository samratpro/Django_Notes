"""____ Warning: It has to run manually ____

____ pip install django-cron ________

... Path = ```settings.py``` ________
INSTALLED_APPS = [
    'django_cron',
]
"""
... Path = ```cron.py``` ________
from django_cron import CronJobBase, Schedule
from .models import ModelName
class ProcessAutomatedTask(CronJobBase):
    schedule = Schedule(run_every_mins=1)
    code = 'myapp.Process_Automated_Task'  # Unique identifier
    def do(self):
        pending_task = ModelName.objects.filter(status='Pending')
        for task in pending_task:
            
            # Process the keyword here using AI API or any other task
            # Update the keyword status to indicate the completion
            
            task.status = 'Completed'
            task.save()

"""
____ python manage.py migrate django_cron ____
____ py manage.py makemigrations ____
____ py manage.py migrate ____

____ python manage.py runcrons ____

"""

