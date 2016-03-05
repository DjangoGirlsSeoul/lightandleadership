from django.db import models
from django.utils import timezone


class OurStory(models.Model):
	img = models.ImageField(upload_to='aboutus', blank=True, null=True)
	text = models.TextField()
	color = models.CharField(max_length=20, blank=True)
	order = models.PositiveIntegerField()



	def __str__(self):
		return self.text


class Ourteam(models.Model):
	img = models.ImageField(upload_to='aboutus', blank=True, null=True)
	text = models.TextField()
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
	text = models.TextField(blank=True, null=True, help_text="Enter a short description of program.")
	color = models.CharField(max_length=20, blank=True, help_text="Both 'red' and '#FF0000' are accceptable")
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