from django import forms
from .models import Project, Rating


class SubmitProjectForm(forms.ModelForm):
    
    class Meta:
        model = Project
        exclude = ("user", )
        fields = ('title', 'landing_page', 'description', 'link', )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'project title'}),
            'link': forms.URLInput(attrs={'placeholder': 'https://project-link.com'}),
            'description': forms.Textarea(attrs={'cols': 20, 'placeholder': 'what is your project all about?'})
        }

class RateProjectForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('design', 'usability', 'content', )
