from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    # Add any additional form fields or customization here
    class Meta:
        model = User
        fields = ['username', 'email']
