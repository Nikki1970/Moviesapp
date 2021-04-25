from django.contrib import admin
from .models import Movie, Studio, Genre, Director
# Register your models here.
admin.site.register(Movie)
admin.site.register(Studio)
admin.site.register(Genre)
admin.site.register(Director)