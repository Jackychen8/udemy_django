# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
	top_name = models.CharField(max_length=264,unique=True)

	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=264,unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage)
	date = models.DateField()

	def __str__(self):
		return str(self.date)

class User(models.Model):
	fName = models.CharField(max_length=128)
	lName = models.CharField(max_length=128)
	email = models.EmailField(max_length=128, unique=True)
	def __str__(self):
		return self.email