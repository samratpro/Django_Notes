# myapp/tasks.py

from celery import shared_task

@shared_task
def your_task_name():
    # Task logic goes here
    pass


# After setup or update -> navigate to your Django project directory, and run the Celery worker
>>> celery -A project_name worker -l info   # replace with your project name


