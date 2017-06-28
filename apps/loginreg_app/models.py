from __future__ import unicode_literals
from django.core.validators import validate_email
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def checks(self, post):
		errors = []

		first_name = post['user_first']
		if len(first_name) <2:
			errors.append("First name is too short")


		last_name = post['user_last']
		if len(last_name) <2:
			errors.append("Last name is too short")


		password = post['user_pass']
		if len(password) <8:
			errors.append("Password is too short")

		email = post['user_email']
		# if not validate_email(email):
		# 	errors.append("Email is not valid")



		if not errors:
			new = User.objects.create(first_name=post['user_first'],
				last_name=post['user_last'],email=post['user_email'],
				password=post['user_pass'])
			debug = {"succeed": True, "data": new}
		else:
			debug = {"succeed": False, "data": errors}
		return debug











class User(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	email = models.CharField(max_length = 30)
	password = models.CharField(max_length = 20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects=UserManager()