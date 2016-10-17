from django.shortcuts import render
from .models import OurStory, OurTeam, EduProgram, EthicalPost, VolunteerPeru, VolunteerOpenPosition, VolunteerAbout, CustomPage, Home, DonateSection, HomeLink
from django.utils import timezone


def our_story(request):
    ourstory = OurStory.objects.all().order_by('order')
    return render(request, 'content/our_story.html', {'ourstory': ourstory})


def our_team(request):
	ourteams = OurTeam.objects.all()
	return render(request, 'content/our_team.html', {'ourteams': ourteams})

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

def volunteer_peru(request):
	volunteerabout = VolunteerAbout.objects.all().order_by('order')
	volunteers = VolunteerPeru.objects.filter(category="Volunteers")
	internships = VolunteerPeru.objects.filter(category="Intership")
	fees = VolunteerPeru.objects.filter(category="Fees")
	positions = VolunteerOpenPosition.objects.all().order_by('date')
	return render(request, 'content/volunteer_peru.html', {'volunteerabout': volunteerabout, 'volunteers': volunteers, 'internships': internships, 'fees': fees, 'positions': positions})

def why_peru(request):
    reasons = CustomPage.objects.filter(category="WhyPeru").order_by('order')
    return render(request, 'content/why_peru.html', {'reasons': reasons})

def financials(request):
	financials = CustomPage.objects.filter(category="Financials").order_by('order')
	return render(request, 'content/financials.html', {'financials': financials})

def donations(request):
	donations = CustomPage.objects.filter(category="Donations").order_by('order')
	return render(request, 'content/donations.html', {'donations': donations})

def volunteer_chicago(request):
	chicago = CustomPage.objects.filter(category="Chicago").order_by('order')
	return render(request, 'content/volunteer_chicago.html', {'chicago': chicago})

def home(request):
    home = Home.objects.all().order_by('order')
    homelink = HomeLink.objects.all().order_by('order')
    return render(request, 'content/home.html', {'home': home, 'homelink': homelink})

def donate(request):
	donateabout = DonateSection.objects.filter(category='AboutUs').order_by('order')
	donate = DonateSection.objects.filter(category='Donate').order_by('order')
	club = DonateSection.objects.filter(category='Club').order_by('order')
	paypal = DonateSection.objects.filter(category='Paypal').order_by('order')
	return render(request, 'content/donate.html', {'donateabout': donateabout, 'donate': donate, 'club': club, 'paypal': paypal})
