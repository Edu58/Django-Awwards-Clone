from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default-website-landing-page.png', upload_to='profile/')
    bio = RichTextField(null=True, blank=True)
    portfolio = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    link = models.URLField(null=True, blank=True)
    landing_page = models.ImageField(default='./static/images/default-website-landing-page.png', upload_to='photos/')
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created_at']

    @classmethod
    def get_project_by_id(cls, project_id):
        project = get_object_or_404(cls, pk=project_id)
        return project

    @classmethod
    def get_project_by_title(cls, title):
        try:
            project = cls.objects.filter(title__icontains=title)
        except:
            return None
        return project

class Rating(models.Model):
    design = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    usability = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    content = models.FloatField(null=False, blank=False, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f'design-{self.design}, usability-{self.usability}, content-{self.content}'

    @classmethod
    def get_rating_average(cls, project_id):
        ratings = cls.objects.filter(project=project_id)
        
        if ratings:
            return ratings
        
        return ratings
