from django.contrib import admin
from moviesapp.models import Category, Actors, Genre, Movies, MovieShorts, RatingStar, Rating, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'description',)
    list_display_links = ('id', 'name', 'url')


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email',)


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'description', 'draft')
    list_filter = ("category", "year",)
    search_fields = ('title', 'category__name')
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors','directors','genres',),)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": (("description", "poster"),)
        }),
        (None, {
            "fields": (("year", "country", "word_premiere"),)
        }),
        (None, {
            "fields": (("directors", "actors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world",),)
        }),
        (None, {
            "fields": (("url", "draft",),)
        }),

    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id',)
    readonly_fields = ('name', 'email',)


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Actors)
admin.site.register(Genre)
# admin.site.register(Movies)
admin.site.register(MovieShorts)
admin.site.register(RatingStar)
admin.site.register(Rating)
# admin.site.register(Reviews)
