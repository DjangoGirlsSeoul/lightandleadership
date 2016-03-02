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
    img = models.ImageField(upload_to='uploads')
    text = models.TextField()
    us_team = models.CharField(max_length=100)
    peru_team = models.CharField(max_length=100)
    board_team = models.CharField(max_length=100)


class OurStoryTitle(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title
