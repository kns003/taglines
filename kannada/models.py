from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    tagline = models.CharField(max_length = 250)

    def __unicode__(self):
        return self.name
    
