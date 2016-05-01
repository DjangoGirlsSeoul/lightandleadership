from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models


class OurStory(models.Model):
	img = models.ImageField(upload_to='aboutus', blank=True, null=True)
	text = tinymce_models.HTMLField(default="")
	color = models.CharField(max_length=20, blank=True)
	order = models.PositiveIntegerField()

	def __str__(self):
		return self.text


class OurTeam(models.Model):
	img = models.ImageField(upload_to='aboutus', blank=True, null=True)
	text = tinymce_models.HTMLField()
	us_team = models.CharField(max_length=100)
	peru_team = models.CharField(max_length=100)
	board_team = models.CharField(max_length=100)


class OurStoryTitle(models.Model):
	title = models.TextField()

	def __str__(self):
		return self.title


class EduProgram(models.Model):
	title = models.CharField(blank=True, null=True, max_length=100)
	img = models.ImageField(upload_to='education',blank=True, null=True, help_text="Only upload an image if order = 1")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description of program.")
	color = models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of the page")
	CHILDREN = "Children"
	TEENS = "Teens"
	WOMEN = "Women"
	ARTISAN = "Artisan"
	POSTCATEGORY = (
		(CHILDREN, 'Children'),
		(TEENS, 'Teens'),
		(WOMEN, 'Women'),
		(ARTISAN, 'Artisan'),
		)
	category = models.CharField(max_length=15, choices=POSTCATEGORY, default=CHILDREN)

	def __str__(self):
		return self.title

class EthicalPost(models.Model):
	title = models.CharField(blank=True, null=True, max_length=100, help_text="If the order number is 1, this will be the page title.")
	img = models.ImageField(upload_to='aboutus',blank=True, null=True, help_text="Upload image corresponding to Text")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description.")
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of the page")



	def __str__(self):
		return self.title

class VolunteerAbout(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of the page")
	title = models.CharField(max_length=100,blank=True, null=True, help_text="If the order number is 1, this will be the page title.")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="For order number 2+: Enter a short description.")
	img = models.ImageField(upload_to='action',blank=True, null=True, help_text="Upload image corresponding to Text")

	def __str__(self):
		return self.title

class VolunteerPeru(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of the page")
	color = models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order is 1 ")
	title = models.CharField(blank=True, null=True, max_length=100, help_text="If the order number is 1, this will be the section title.")
	img = models.ImageField(upload_to='action',blank=True, null=True, help_text="Upload image corresponding to Text")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description")
	VOLUNTEERS = "Volunteers"
	INTERNSHIP = "Intership"
	FEES = "Fees"
	POSTCATEGORY = (
		(VOLUNTEERS, 'Volunteers'),
		(INTERNSHIP, 'Intership'),
		(FEES, 'Fees'),
		)
	category = models.CharField(max_length=15, choices=POSTCATEGORY, default=VOLUNTEERS)

	def __str__(self):
		return self.title

class VolunteerOpenPosition(models.Model):
	title = models.CharField(blank=True, max_length=100, help_text="Please enter the position title")
	date = models.DateTimeField(default=timezone.now, help_text="Please enter the start date for the position")
	link = models.URLField(max_length=200, help_text="Please enter a link for the application")

	def __str__(self):
		return self.title

class CustomPage(models.Model):
	CHICAGO = "Chicago"
	DONATIONS = "Donations"
	FINANCIALS = "Financials"
	WHYPERU = "WhyPeru"
	POSTCATEGORY = (
		(CHICAGO, 'Chicago'),
		(DONATIONS, 'Donations'),
		(FINANCIALS, 'Financials'),
		(WHYPERU, 'WhyPeru'),
		)
	category = models.CharField(max_length=15, choices=POSTCATEGORY, default=CHICAGO )
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of the page")
	title = models.CharField(blank=True, null=True, max_length=100, help_text="If the order number is 1, this will be the page title.")
	img = models.ImageField(upload_to='volunteer',blank=True, null=True, help_text="Upload image corresponding to Text")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description.")

	def __str__(self):
		return self.title

class FooterInfo(models.Model):
	img = models.ImageField(upload_to='volunteer',blank=True, null=True, help_text="Upload image for footer")
	title = models.CharField(blank=True, null=True, max_length=100, help_text="Enter Footer Title")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description.")
	learnmorelink = models.CharField(default="#", max_length=200)
	facebooklink =  models.URLField(default="#")
	twitterlink = models.URLField(default="#")
	instagramlink = models.URLField(default="#")

	def __str__(self):
		return self.title
