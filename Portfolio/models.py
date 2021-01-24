from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    photo = models.ImageField(upload_to='portfolio/images',default='portfolio/images/Watch-this-space.jpg')
    url = models.URLField(blank = True)

    def __str__(self):
    	return self.title