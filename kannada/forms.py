from django import forms
from kannada.models import Movie


class MovieForm(forms.Form):
	movie_name = forms.CharField(
				label = "Movie Name", 
        		widget = forms.TextInput()
    )
