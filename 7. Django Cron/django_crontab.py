"""
pip install django-crontab

Path = ```settings.py```
INSTALLED_APPS = [
    'django_crontab',
]

CRONJOBS = [
    ('*/1 * * * *', 'app.cron.ProcessAutomatedTask')
]

"""
``` .... Path = cron.py  ``
from .models import ModelName
class ProcessAutomatedTask(CronJobBase):
    code = 'myapp.Process_Automated_Task'  # Unique identifier
    def do(self):
        pending_keywords = ModelName.objects.filter(status='Pending')
        for task in pending_task:
            
            # Process the keyword here using AI API or any other task
            # Update the keyword status to indicate the completion
            
            task.status = 'Completed'
            task.save()

"""
python manage.py makemigrations
python manage.py migrate


python manage.py crontab add


___ python manage.py crontab show _____
___ python manage.py crontab show ____


"""
