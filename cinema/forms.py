from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'poster', 'trailer_url', 'release_date',
                  'duration', 'ticket_price', 'is_3d', 'age_restriction', 'imdb_rating']
        widgets = {
            'ticket_price': forms.DecimalInput(attrs={'min': 0.01})  
        }
