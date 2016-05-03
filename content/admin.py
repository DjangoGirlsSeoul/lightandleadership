from django.contrib import admin

from .models import OurStory, OurTeam, EduProgram, EthicalPost, VolunteerPeru, VolunteerOpenPosition, VolunteerAbout, CustomPage,Home,FooterInfo
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from content.forms import OurTeamForm


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['order', 'img', 'text']
    list_display=('order','img','text')

class HomeAdmin(admin.ModelAdmin):
    fields = ['title','color','order','img','text']
    list_display=('title','color','order','img','text')

class OurTeamAdmin(admin.ModelAdmin):
    form = OurTeamForm
    list_display = ('text','us_team', 'peru_team', 'board_team')

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('category', 'order','title')


class EthicalPostAdmin(admin.ModelAdmin):
    fields = ['order', 'title', 'img', 'text']
    list_display = ('order', 'title' )

class MCEFlatPageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        exclude = []


class MCEFlatPageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = MCEFlatPageForm


class VolunteerPeruAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'color', 'title', 'img', 'text']
    list_display = ('category', 'order','title')

class VolunteerOpenPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

class VolunteerAboutAdmin(admin.ModelAdmin):
    list_display = ('order', 'title' )

class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('category', 'order','title')


admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EthicalPost, EthicalPostAdmin)
admin.site.register(VolunteerAbout, VolunteerAboutAdmin)
admin.site.register(VolunteerPeru, VolunteerPeruAdmin)
admin.site.register(VolunteerOpenPosition, VolunteerOpenPositionAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(FooterInfo)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MCEFlatPageAdmin)
