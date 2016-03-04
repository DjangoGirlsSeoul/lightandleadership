from django.shortcuts import render
from .models import OurStory, Ourteam, ChildrensProgram
from django.utils import timezone


def our_story(request):
    ourstory = OurStory.objects.all().order_by('order')
    return render(request, 'content/our_story.html', {'ourstory': ourstory})


def our_team(request):
    return render(request, 'content/our_team.html', {})

def childrens_program(request):
	childrensprograms = ChildrensProgram.objects.all().order_by('order')
	return render(request, 'content/childrensprogram.html', {'childrensprograms': childrensprograms })
