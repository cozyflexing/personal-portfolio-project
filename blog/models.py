from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)
