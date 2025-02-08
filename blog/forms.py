from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post  # Ensure Post model is correctly imported

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):  # Add this class
    class Meta:
        model = Post
        fields = ['title', 'content']  # Include other fields as needed
