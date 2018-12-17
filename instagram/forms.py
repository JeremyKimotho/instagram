from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=254, help_text='Required. Please use a valid email address')

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude=['likes', 'slug','profile', 'posted_at']