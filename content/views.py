from django.shortcuts import render
from .models import OurStory
from django.utils import timezone

# Create your views here.
def our_story(request):
	ourstory = OurStory.objects.all()
	return render(request, 'content/our_story.html', {'ourstory': ourstory})
	