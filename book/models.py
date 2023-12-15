from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Title(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class BookAuthor(models.Model):
    book_author = models.CharField(max_length=100)

    def __str__(self):
        return self.book_author

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre   

class Book(models.Model):
    title=models.CharField(max_length=100)
    #title=models.ForeignKey(Title, on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    book_author = models.CharField(max_length=100, null=True)
    #book_author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, default=0)
    genre=models.CharField(max_length=100)
    #genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    review=models.TextField(null=True)
    release_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})

