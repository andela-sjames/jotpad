# Create your models here.

from django.db import models

class Note(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created']
