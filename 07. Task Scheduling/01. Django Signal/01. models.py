from django.db import models

class InfoBulkModel(models.Model):
    user = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
