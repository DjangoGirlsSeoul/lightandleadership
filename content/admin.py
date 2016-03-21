from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram, EthicalPost
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

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


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MCEFlatPageAdmin)
>>>>>>> master

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')

class OurStoryAdmin(admin.ModelAdmin):
    fields = [ 'order', 'img', 'color', 'text']
    list_display = ('order', 'color')

admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EthicalPost)
