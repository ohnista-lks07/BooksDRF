from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    birth_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
    )
    year = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_books',
    )

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return f"{self.title} ({self.year})"

