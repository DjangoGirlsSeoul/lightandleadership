from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram
from content.forms import OurTeamForm


class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['order','text']
    list_display=('order', 'text')


class OurTeamAdmin(admin.ModelAdmin):
    form = OurTeamForm
    list_display = ('text','us_team', 'peru_team', 'board_team')


admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
