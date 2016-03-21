from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram, EthicalPost
# Register your models here.

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


admin.site.register(OurStory)
admin.site.register(OurTeam)
admin.site.register(EduProgram, EduProgramAdmin)
admin.site.register(EthicalPost)
