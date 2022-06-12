from django import forms
from .models import Project, Rating
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password', 'password1']


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label= 'Password',widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields = ['username', 'password']


class SubmitProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        exclude = ("user", )
        fields = ('title', 'landing_page', 'description', 'link', )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'project title'}),
            'link': forms.URLInput(attrs={'placeholder': 'https://project-link.com'}),
            'description': forms.CharField(widget=CKEditorWidget())
        }

class RateProjectForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content', )
        widgets = {
            'design': forms.NumberInput(attrs={'min':0, 'max':10}),
            'usability': forms.NumberInput(attrs={'min': 0, 'max': 10}),
            'content': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }