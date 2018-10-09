from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Reviewer


class ReviewerCreationForm(UserCreationForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput())

	class Meta(UserCreationForm.Meta):
		model = Reviewer
		fields = '__all__'


	def clean_password(self):
		password = self.cleaned_data.get("password")
		if not password1:
			raise forms.ValidationError("Passwords don't match")
		return password1

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


class ReviewerChangeForm(UserChangeForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)


	class Meta(UserChangeForm.Meta):
		model = Reviewer
		fields = '__all__'


	def clean_password(self):
		password = self.cleaned_data.get("password")
		if not password:
			raise forms.ValidationError("Passwords don't match")
		return password

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user