from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


from moviesapp.models import Movies


# class MoviesViews(View):
class MoviesViews(ListView):
    """Список фильмов"""
    model = Movies
    gueryset = Movies.objects.filter(draft=False)
    template_name = 'moviesapp/movie_list.html'

    # def get(self, request):
    #     print('asdadadsads')
    #     moviesapp = Movies.objects.all()
    #     context = {'movie_list': moviesapp}
    #     return render(request, 'moviesapp/movie_list.html', context)


# class MovieDitailsView(View):
class MovieDitailsView(DetailView):
    """Детальное описание фильма"""
    model = Movies
    template_name = 'moviesapp/movie_detail.html'
    slug_field = 'url'


    # def get(self, request, slug):
    #     movie = Movies.objects.get(url=slug)
    #     context = {'movie': movie}
    #
    #     return render(request, 'moviesapp/movie_detail.html', context)
