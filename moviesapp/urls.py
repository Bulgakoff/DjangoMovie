from django.urls import path
import moviesapp.views as movieapp

app_name = 'movieapp'

urlpatterns = [
    path('', movieapp.MoviesViews.as_view(), name='main'),
    path('<slug:slug>/', movieapp.MovieDitailsView.as_view(), name='details_movies'),

]
