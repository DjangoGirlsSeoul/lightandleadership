from django.db import models
from django.utils import timezone


class Ourstory(models.Model):
    img = models.ImageField(upload_to ='uploads')
    text = models.TextField()
    color = models.CharField(max_length=6)



    def __str__(self):
        return self.text
