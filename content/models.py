from django.db import models
from django.utils import timezone


class OurStory(models.Model):
    img = models.ImageField(blank=True, null=True)
    text = models.TextField()
    color = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField()



    def __str__(self):
        return self.text

class OurStoryTitle(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title