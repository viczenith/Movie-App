from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to='review_images/', blank=True, null=True) 
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} Review {self.pk}"

