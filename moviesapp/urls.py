from django.urls import path
import moviesapp.views as movieapp

app_name = 'movieapp'

urlpatterns = [
    path('', movieapp.MoviesViews.as_view(), name='main'),
    path('<slug:slug>/', movieapp.MovieDitailsView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', movieapp.AddReviews.as_view(), name='add_reviews_movie_detail'),

]
