from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.

GENRE_CHOICES=[
        ('Fiction','Fiction'),
        ('Non_fiction','Non_fiction'),
        ('Science','Science'),
        ('Other','Other'),
    ]


class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publication_date = models.DateField()
    average_rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(5)],
        default=0
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk": self.pk})
    
