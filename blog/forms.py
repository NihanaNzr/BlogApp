from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post  
from ckeditor.widgets import CKEditorWidget

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Enable CKEditor in forms

    class Meta:
        model = Post
        fields = ['title', 'content']