from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label="Никнейм/Username/Нікнейм", required=True)
	first_name = forms.CharField(label="Имя/First name/Імʼя", required=True)
	last_name = forms.CharField(label="Фамилия/Last name/Прізвище", required=True)



	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class UserProfile(UserChangeForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label="Никнейм/Username/Нікнейм", required=True)
	first_name = forms.CharField(label="Имя/First name/Імʼя", required=True)
	last_name = forms.CharField(label="Фамилия/Last name/Прізвище", required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email")

	def save(self, commit=True):
		user = super(UserProfile, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user