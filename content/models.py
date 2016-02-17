from django.db import models
from django.utils import timezone


class OurStory(models.Model):
    img = models.ImageField(blank=True, null=True)
    text = models.TextField()
    color = models.CharField(max_length=6, blank=True)
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    ORDER = (
    	(FIRST, 'first'),
    	(SECOND, 'second'),
    	(THIRD, 'third'),
    	)
    order = models.CharField(max_length=7, choices=ORDER, default=FIRST)



    def __str__(self):
        return self.text
