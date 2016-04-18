from django.shortcuts import render
from .models import OurStory, OurTeam, EduProgram, EthicalPost
from django.utils import timezone


def our_story(request):
    ourstory = OurStory.objects.all().order_by('order')
    return render(request, 'content/our_story.html', {'ourstory': ourstory})


def our_team(request):
    return render(request, 'content/our_team.html', {})

def childrens_program(request):
	childrensprograms = EduProgram.objects.filter(category="Children").order_by('order')
	return render(request, 'content/childrensprogram.html', {'childrensprograms': childrensprograms })

def teens_program(request):
	teensprograms = EduProgram.objects.filter(category="Teens").order_by('order')
	return render(request, 'content/teensprogram.html', {'teensprograms': teensprograms })

def womens_program(request):
	womensprograms = EduProgram.objects.filter(category="Women").order_by('order')
	return render(request, 'content/womensprogram.html', {'womensprograms': womensprograms })

def artisan_program(request):
	artisanprograms = EduProgram.objects.filter(category="Artisan").order_by('order')
	return render(request, 'content/artisanprogram.html', {'artisanprograms': artisanprograms })



def ethical_post(request):
    ethicalpost = EthicalPost.objects.all().order_by('order')
    return render(request, 'content/ethical_page.html', {'ethicalpost': ethicalpost})
