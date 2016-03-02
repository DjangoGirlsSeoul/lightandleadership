from django.db import models
from django.utils import timezone


class OurStory(models.Model):
    img = models.ImageField(blank=True, null=True)
    text = models.TextField()
    color = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField()



    def __str__(self):
        return self.text


class Ourteam(models.Model):
    img = models.ImageField(blank=True, null=True)
    text = models.TextField()
    us_team = models.CharField(max_length=100)
    peru_team = models.CharField(max_length=100)
    board_team = models.CharField(max_length=100)


class OurStoryTitle(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

class ChildrensProgram(models.Model):
	pagetitle = models.CharField(blank=True, null=True, max_length=100)
	img = models.ImageField(blank=True, null=True)
	subtitle = models.CharField(blank=True, null=True, max_length=50)
	text = models.TextField(blank=True, null=True)
	color = models.CharField(max_length=20, blank=True)
	order = models.PositiveIntegerField()

	def __str__(self):
		if self.pagetitle:
			return self.pagetitle
		else:
			return self.subtitle