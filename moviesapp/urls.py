from django.urls import path
import moviesapp.views as movieapp

app_name = 'movieapp'

urlpatterns = [
    path('', movieapp.MoviesViews.as_view(),)

]
