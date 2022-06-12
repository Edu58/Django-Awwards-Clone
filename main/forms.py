from django import forms
from .models import Project, Rating
from ckeditor.widgets import CKEditorWidget


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