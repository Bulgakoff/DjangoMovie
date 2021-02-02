from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from moviesapp.forms import ReviewsForm
from moviesapp.models import Movies, Category, Actors


# class MoviesViews(View):
class MoviesViews(ListView):
    """Список фильмов"""
    model = Movies
    gueryset = Movies.objects.filter(draft=False)
    template_name = 'moviesapp/movie_list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(MoviesViews, self).get_context_data(*args, **kwargs)
    #     context.update({'categories': Category.objects.all()})
    #     return context

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


class AddReviews(View):
    """Отправка отзывов"""

    def post(self, request, pk):
        # form = ReviewsForm(request.POST)
        # if form.is_valid():
        #     form = form.save(commit=False)
        #     form.movie_id = pk
        #     form.save()
        #
        # return redirect('/')

        form = ReviewsForm(request.POST)
        movie = Movies.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ActorViews(DetailView):
    """вывод инфы об актере"""
    model = Actors
    template_name = 'moviesapp/actor.html'
    slug_field = 'name' # поле по которому будем искать  актеров
