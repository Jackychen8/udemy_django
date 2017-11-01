from django.db import models

# Create your models here.
class User(models.Model):
	fName = models.CharField(max_length=128)
	lName = models.CharField(max_length=128)
	email = models.EmailField(max_length=128, unique=True)
	def __str__(self):
		return self.email