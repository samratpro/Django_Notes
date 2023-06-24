# cron.py in_app_folder

from django_cron import CronJobBase, Schedule
from .models import ModelName

class ProcessAutomatedTask(CronJobBase):
    RUN_EVERY_MINS = 1  # Set the frequency of the cron job

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'myapp.process_keywords_job'  # Unique identifier for your cron job

    def do(self):
        # Retrieve all pending keywords from the database
        pending_keywords = Keyword.objects.filter(status='Pending')
        
        for keyword in pending_keywords:
            # Process the keyword here using AI API or any other task
            # Update the keyword status to indicate completion
            keyword.status = 'Completed'
            keyword.save()

