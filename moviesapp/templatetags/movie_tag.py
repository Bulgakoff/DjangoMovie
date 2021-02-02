from django import template

from moviesapp.models import Category, Movies

register = template.Library()


@register.simple_tag()
def get_categories():
    """return list our categories"""
    return Category.objects.all()

@register.inclusion_tag('moviesapp/tags/last_movies.html')
def get_last_movies(count=5):
    movies= Movies.objects.order_by('id')[:count]
    context = {
        'last_movies':movies
    }
    return context
