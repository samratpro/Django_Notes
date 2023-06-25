# Step : 1
pip install celery
pip install redis


## Project Directory
# create new file name: celery.py
```
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectName.settings')
app = Celery('ProjectName')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```
## Project Directory
# Existing file name: __init__.py:
```
from .celery import app as celery_app
__all__ = ('celery_app',)
```

