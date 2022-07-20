from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=255)
    reading = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE, null=True, blank=True)
    date_started = models.DateField(auto_now_add=True, null=True, blank=True)
    date_finished = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=255, null=True, blank=True)
