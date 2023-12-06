from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InfoBulkModel

# This function will perform the job when a keyword becomes 'Pending'
def perform_job(pending_keyword):
    # Your job logic here
    print(f"Performing job for keyword: {pending_keyword}")

# Define a signal receiver
@receiver(post_save, sender=InfoBulkModel)
def keyword_status_changed(sender, instance, created, **kwargs):
    if created and instance.status == 'Pending':
        perform_job(instance.keyword)
