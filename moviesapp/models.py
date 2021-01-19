from django.db import models
from datetime import date
from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your models here.
class Category(models.Model):
    """категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actors(models.Model):
    "Актеры и режисеры"
    name = models.CharField("ИМЯ", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение-url", upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер и режисер'
        verbose_name_plural = 'Актеры и режисеры'


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Наименование жанра", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movies(models.Model):
    """Фильмы"""
    title = models.CharField('Название фильма', max_length=100)
    tagline = models.CharField('Слоган фильма', max_length=100, default='')
    description = models.TextField("Описание фильма")
    poster = models.ImageField('Постер фильма', upload_to='moviesapp/')
    year = models.PositiveSmallIntegerField("Год выпуска фильма", default=2019)
    country = models.CharField('Страна фильма', max_length=30)
    directors = models.ManyToManyField(Actors, verbose_name='режисер', related_name='film_director')
    actors = models.ManyToManyField(Actors, verbose_name='актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='film_genre')
    word_premiere = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Буджет фильма', default=0, help_text='указывать сумму в долларах')
    fees_in_usa = models.PositiveIntegerField(
        'сборы в США', default=0, help_text='указывать сумму в долларах')
    fees_in_world = models.PositiveIntegerField(
        'сборы в мире', default=0, help_text='указывать сумму в долларах')
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        context = {'slug': self.url}
        return reverse('movieapp:details_movies', kwargs=context)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MovieShorts(models.Model):
    """Кадры из фильма"""
    title = models.CharField('Заголовок фильма', max_length=100)
    description = models.TextField("Описание фильма")
    image = models.ImageField("Изображение", upload_to='movie_shots/')
    movie = models.ForeignKey(Movies, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из Фильма'
        verbose_name_plural = 'Кадры из Фильма'


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.PositiveSmallIntegerField('Значение рейтинга', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, verbose_name='фильм')

    def __str__(self):
        return f'{self.star}--{self.movie}'

    class Meta:
        verbose_name = 'Рейтинг '
        verbose_name_plural = 'Рейтинги'


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщегние отзыва', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='РОдитель', on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movies, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}---{self.movie}'

    class Meta:
        verbose_name = 'Отзыв '
        verbose_name_plural = 'Отзывы'
