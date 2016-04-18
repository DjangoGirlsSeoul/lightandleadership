from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from content.forms import OurTeamForm
from .models import OurStory, OurTeam, EduProgram, EthicalPost


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['order','text']
    list_display=('order', 'text')


class OurTeamAdmin(admin.ModelAdmin):
    form = OurTeamForm
    list_display = ('text','us_team', 'peru_team', 'board_team')


class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


class EthicalPostAdmin(admin.ModelAdmin):
    fields = ['order', 'title', 'img', 'text']
    list_display = ['title', 'order']


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


admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EthicalPost, EthicalPostAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MCEFlatPageAdmin)