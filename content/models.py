from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from django.utils.safestring import mark_safe


class OurStory(models.Model):
	img = models.ImageField(upload_to='aboutus', blank=True, null=True)
	text = tinymce_models.HTMLField(default="")
	color = models.CharField(max_length=20, blank=True)
	order = models.PositiveIntegerField()

	def __str__(self):
		return self.text

class Home(models.Model):
	title = models.CharField(blank=True, null=True, max_length=100)
	color = models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")
	order = models.PositiveIntegerField()
	img = models.ImageField(upload_to='aboutus', blank=True, null=True,help_text="Image is optional. If there is no image, this section will be full width")
	text = tinymce_models.HTMLField(default="")
	link = models.URLField(max_length=200, help_text="Please enter a link for learn more button", blank=True, null=True)
	button_text = models.CharField(blank=True, null=True, max_length=100, default="Learn More")
	link2 = models.URLField(max_length=200, blank=True, null=True, help_text="Please enter a link for learn more button", )
	button_text2 = models.CharField(blank=True, null=True, max_length=100, default="Learn More")

	def __str__(self):
		return self.title


class OurTeam(models.Model):
	title = models.CharField(default="Our Team", max_length=200)
	img = models.ImageField(upload_to='aboutus', blank=True, null=True, help_text="This will be the page title image.")
	text = tinymce_models.HTMLField()
	us_team = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description")
	peru_team = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description")
	board_team = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description")



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
	video = models.BooleanField(default=False, help_text="check here if you want this section to be full width")
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
	copyright = models.CharField(default=" ", max_length=300)

	def __str__(self):
		return self.text

class DonateSection(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be at the top of each section(section order: aboutus, donate, club, paypal")
	color = models.CharField(max_length=20, blank=True, help_text="This is the background color for section titles, Only needed if order = 1.")
	title = models.CharField(blank=True, null=True, max_length=100, help_text="If the order number is 1, this will be the section title.")
	img = models.ImageField(upload_to='action',blank=True, null=True, help_text="Upload image corresponding to Text")
	text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description")
	paypal_button = models.TextField(blank=True, null=True, help_text="enter the paypal code if you want it in this section.")
	ABOUTUS = "AboutUs"
	DONATE = "Donate"
	CLUB = "Club"
	PAYPAL = "Paypal"
	POSTCATEGORY = (
		(ABOUTUS, 'AboutUs'),
		(DONATE, 'Donate'),
		(CLUB, 'Club'),
		(PAYPAL, 'Paypal'),
		)
	category = models.CharField(max_length=15, choices=POSTCATEGORY, default=DONATE)

	def __str__(self):
		return self.title

class Menu(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be on the left.")
	title = models.CharField(null=True, max_length=100)
	link = models.CharField(blank=True, null=True, max_length=100)

	def __str__(self):
		return self.title

class SubMenu(models.Model):
	order = models.PositiveIntegerField(help_text="Enter a number. 1 will be on the top of a dropdown.")
	title = models.CharField(null=True, max_length=100)
	link = models.CharField(blank=True, null=True, max_length=100)
	menu = models.ForeignKey(
        'Menu',
        on_delete=models.CASCADE,
    )

	def __str__(self):
		return self.title

class HomeLink(models.Model):
	link = models.URLField(max_length=200, help_text="Please enter a link")
	title = models.CharField(blank=True, null=True, max_length=100)
	color = models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")
	order = models.PositiveIntegerField(default=1)
	icon = models.CharField(blank=True, null=True, max_length=100, default="fa-heart", help_text=mark_safe("Please write in which icon you'd like, ie fa-phone. Check <a href='http://fontawesome.io/icons/'>here</a> for icons."))

	def __str__(self):
		return self.title

class Apply(models.Model):
	title = models.CharField(max_length=100, help_text="not required but helpful", blank=True, null=True)
	text = models.TextField(help_text="please enter the code for the embedded application here")

	def __str__(self):
		return self.text
