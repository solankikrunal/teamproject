from __future__ import unicode_literals
from django.db import models



class SignUP(models.Model):
	first_name=models.Charfield(max_length=120)
	last_name=models.Charfield(max_length=120)
	email=models.EmailField()
	password=models.Charfield(max_length=60)

	def __unicode__(self)
		return self.email

