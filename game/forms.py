from django import forms

class GameForm(forms.Form):
    player_white = forms.CharField(max_length=25, required=False)
    player_black = forms.CharField(max_length=25, required=False)