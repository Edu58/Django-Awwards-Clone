from dataclasses import fields
from django import forms
from .models import Project


class SubmitProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        exclude = ("user", )
        fields = ('title', 'landing_page', 'description', 'link', )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'project title'}),
            'link': forms.URLInput(attrs={'placeholder': 'project link'}),
            'description': forms.Textarea(attrs={'cols': 20, 'placeholder': 'what is your project all about?'})
        }