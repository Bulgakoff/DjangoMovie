from django.contrib import admin
from moviesapp.models import Category, Actors, Genre, Movies, MovieShorts, RatingStar, Rating, Reviews

# Register your models here.
admin.site.register(Category)
admin.site.register(Actors)
admin.site.register(Genre)
admin.site.register(Movies)
admin.site.register(MovieShorts)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
