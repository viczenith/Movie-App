from django import forms
from .models import *

class MovieSearchForm(forms.Form):
    title = forms.CharField(required=False)
    genre = forms.CharField(required=False)
    release_year = forms.IntegerField(required=False)
    director = forms.CharField(required=False)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment', 'image']

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['title', 'content', 'rating']
