from django import forms
from django.core import checks
from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram
from django.forms import TextInput, Textarea
# Register your models here.

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['order','text']
    list_display=('order', 'text')


class OurTeamForm(forms.ModelForm):
    model = OurTeam
    fields = ['text','us_team', 'peru_team', 'board_team']


class OurTeamAdmin(admin.ModelAdmin):
    fields = ['text','us_team', 'peru_team', 'board_team']
    list_display = ('text','us_team', 'peru_team', 'board_team')


admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
