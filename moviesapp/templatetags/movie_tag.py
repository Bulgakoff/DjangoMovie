from django import template

from moviesapp.models import Category, Movies

register = template.Library()


@register.simple_tag()
def get_categories():
    """return list our categories возвращает во все шаблоны приложения (dry) """
    return Category.objects.all()

@register.inclusion_tag('moviesapp/tags/last_movies.html')
def get_last_movies(count=5):
    """ вывод последних фильмов в данном случае 5"""
    movies= Movies.objects.order_by('id')[:count]
    context = {
        'last_movies':movies
    }
    return context
