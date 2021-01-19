from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from moviesapp.models import Category, Actors, Genre, Movies, MovieShorts, RatingStar, Rating, Reviews


# from post.models import Post

class MoviesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movies
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name', 'url', 'description',)
    list_display_links = ('id', 'name', 'url')


class MoviesShortInLine(admin.TabularInline):
    model = MovieShorts
    extra = 1

    readonly_fields = ('get_image',)

    def get_image(self, obj_model_mshort):
        return mark_safe(f'<img src={obj_model_mshort.image.url} width="50" height="60">')

    get_image.short_description = "Изобр"


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email',)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    """Фильмы"""
    list_display = ('title', 'category', 'url', 'description', 'draft')
    list_filter = ("category", "year",)
    search_fields = ('title', 'category__name')
    inlines = [MoviesShortInLine, ReviewInLine, ]
    save_on_top = True
    save_as = True
    form = MoviesAdminForm
    actions = ['publish','unpublish']
    list_editable = ('draft',)
    # fields = (('actors','directors','genres',),)
    fieldsets = (
        ("Название слоган", {
            "fields": (("title", "tagline",),),
        }),
        ("Description", {
            "classes": ("collapse",),
            "fields": ("description", ("poster", "get_image")),
        }),
        (None, {
            "fields": (("year", "country", "word_premiere",),),
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("directors", "actors", ("genres", "category"))),
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world",),),
        }),
        ("Опции", {
            "fields": (("url", "draft",),),
        }),

    )
    readonly_fields = ('get_image',)

    def get_image(self, obj_model_actor_poster):
        return mark_safe(f'<img src={obj_model_actor_poster.poster.url} width="100" height="100">')

    get_image.short_description = "Постер"

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')


    publish.short_description='Опубликовать'
    publish.allowed_permissions=('change',)

    unpublish.short_description='Снять с публикации'
    unpublish.allowed_permissions=('change',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('name', 'email', 'parent', 'movie', 'id',)
    readonly_fields = ('name', 'email',)
    save_on_top = True
    # fieldsets = (
    #     ("Отзывы", {
    #         "classes": ("collapse",),
    #         "fields": (("name", "email","text", "parent","movie", "id",),),
    #     }),
    # )


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    """Актеры"""
    list_display = ('name', 'age', 'description', 'get_image', 'image',)
    readonly_fields = ('get_image', 'name',)

    def get_image(self, obj_model_actors):
        return mark_safe(f'<img src={obj_model_actors.image.url} width="50" height="60">')

    get_image.short_description = "Изображения"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('name', 'url', 'description',)


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Рейтинг """
    list_display = ('value',)


@admin.register(MovieShorts)
class MovieShortsAdmin(admin.ModelAdmin):
    """Кадры из фильмов"""

    list_display = ('title', 'movie', 'description', 'image', 'get_movie_short')
    readonly_fields = ('get_movie_short',)
    fieldsets = (
        ("Кадры из фильма", {
            "classes": ("collapse",),
            "fields": (('title', 'movie', 'description', 'image', 'get_movie_short'),),
        }),
    )

    def get_movie_short(self, obj_model_movie_short):
        return mark_safe(f'<img src={obj_model_movie_short.image.url} width="50" height="60">')

    get_movie_short.short_description = "Кадры из фильмов"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('ip', 'star', 'movie',)


admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Actors)
# admin.site.register(Genre)
# admin.site.register(Movies)
# admin.site.register(MovieShorts)
# admin.site.register(RatingStar)
# admin.site.register(Rating)
# admin.site.register(Reviews)
