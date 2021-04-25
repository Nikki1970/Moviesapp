from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=100)
    subtitle = models.BooleanField(null=True)
    slug = models.SlugField(max_length=250)
    directors = models.ManyToManyField('Director')
    studio = models.ForeignKey('Studio',on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to="Moviesapp/static/images",null=True,blank=True)
    released_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    ASIN = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def amazon_url(self):
        return "https://www.amazon.com/dp/" + self.ASIN


class Studio(models.Model):
    title = models.CharField(max_length=70)
    prefix = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    slug = models.SlugField(max_length = 250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Studio, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Director(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.PositiveIntegerField(validators=[MinValueValidator(1000000000),MaxValueValidator(100000000000)])
    birth_date = models.DateField()
    website = models.URLField(max_length=100)
    gender_choices = [
        ('M','Male'),
        ('F','Female'),
    ]
    gender = models.CharField(max_length=1,choices=gender_choices, blank=True)

    def __str__(self):
        return self.last_name
    
class Review(models.Model):
    film = models.ForeignKey('Movie',on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.review