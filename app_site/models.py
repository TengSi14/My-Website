from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=100)
    msg = models.TextField()
    pub_date = models.DateField()