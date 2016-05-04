from django import forms
from django.forms import ModelForm, Textarea
from .models import OurTeam


class OurTeamForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, help_text="This will be the title and header info. You can use HTML tags.")
    us_team = forms.CharField(widget=forms.Textarea, help_text="Write one name per line. You can leave one blank line between if you'd like more space between names.")
    peru_team = forms.CharField(widget=forms.Textarea, help_text="Write one name per line. You can leave one blank line between if you'd like more space between names.")
    board_team = forms.CharField(widget=forms.Textarea, help_text="Write one name per line. You can leave one blank line between if you'd like more space between names.")

