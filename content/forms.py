from django import forms
from django.forms import ModelForm, Textarea
from .models import OurTeam


class OurTeamForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    us_team = forms.CharField(widget=forms.Textarea)
    peru_team = forms.CharField(widget=forms.Textarea)
    board_team = forms.CharField(widget=forms.Textarea)

