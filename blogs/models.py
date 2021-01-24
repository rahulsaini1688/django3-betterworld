from django.db import models

# Create your models here.

class Blog(models.Model):
	"""docstring for ClassName"""
	topic = models.CharField(max_length=30)
	blog_description = models.CharField(max_length=60)
	blog_post_date = models.DateField()

	def __str__(self):
		return self.topic