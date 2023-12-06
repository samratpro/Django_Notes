from django.db import models

class InfoBulkModel(models.Model):
    user = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Call the original save() method to save the instance
        super(InfoBulkModel, self).save(*args, **kwargs)

        # Perform the job/function here after saving
        if self.status == 'Pending':
            perform_job(self.keyword)  # Call your job function passing the keyword
