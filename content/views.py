from django.shortcuts import render
from .models import Ourstory, Ourteam

def our_story(request):
    return render(request, 'content/our_story.html', {})


def our_team(request):
    return render(request, 'content/our_team.html', {})