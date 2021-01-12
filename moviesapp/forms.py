from django import forms
from moviesapp.models import Reviews


class ReviewsForm(forms.ModelForm):
    """Форма отзывов"""
    class Meta:
        model= Reviews
        fields = ('name','email','text',)