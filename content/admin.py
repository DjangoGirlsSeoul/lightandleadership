from django.contrib import admin
from .models import OurStory, Ourteam, EduProgram
# Register your models here.

class EduProgramAdmin(admin.ModelAdmin):
    fields = ['category', 'order', 'title', 'img', 'color', 'text']
    list_display = ('title','category', 'order')


admin.site.register(OurStory)
admin.site.register(Ourteam)
admin.site.register(EduProgram, EduProgramAdmin)
