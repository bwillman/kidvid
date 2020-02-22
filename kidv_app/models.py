from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
	embed_tag = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.embed_tag