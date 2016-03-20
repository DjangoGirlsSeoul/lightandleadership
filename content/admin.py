from django.contrib import admin
from .models import OurStory, OurTeam, EduProgram
# Register your models here.

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


class OurStoryAdmin(admin.ModelAdmin):
    fields = ['id','order','text']
    list_display=('id', 'order', 'text')



admin.site.register(OurStory, OurStoryAdmin)
admin.site.register(OurTeam)
admin.site.register(EduProgram, EduProgramAdmin)
