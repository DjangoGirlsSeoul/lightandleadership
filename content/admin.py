from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram
# Register your models here.

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['id','order','text']
    list_display=('id', 'order', 'text')


class OurTeamAdmin(admin.ModelAdmin):
    fields = ['id', 'text']
    list_display = ('id', 'text')

admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(EduProgram, EduProgramAdmin)
