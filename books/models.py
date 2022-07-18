from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=255)

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    reviewer = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE, null=True, blank=True)

class ReadingBook(models.Model):
    book = models.ForeignKey(Book, related_name="reading_books", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reading_books", on_delete=models.CASCADE, null=True, blank=True)
    date_started = models.DateField(auto_now_add=True)
    date_finished = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=255, null=True, blank=True)
