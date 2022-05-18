from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#sign up form
class SignUpForm(UserCreationForm):
	class meta:
		model = User
		fields=("username","password1","password2")

	def save(self, commit: bool = True):
		user = super(SignUpForm,self).save(commit=False)
		user.save()
		return user
