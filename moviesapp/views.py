from django.shortcuts import render
from django.views.generic.base import View

from moviesapp.models import Movies

class MoviesViews(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movies.objects.all()
        context = {'movie_list':movies}
        return render(request, 'moviesapp/movie_list.html', context)
