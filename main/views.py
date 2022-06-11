from django.shortcuts import get_object_or_404, redirect, render
from .forms import RateProjectForm, SubmitProjectForm
from .models import Profile, Project, Rating
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'home.html', context)

def submit(request):
    form = SubmitProjectForm()

    current_user = request.user
    if request.method == "POST":
        form = SubmitProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    context = {
        'form': form
    }
    
    return render(request, 'submit.html', context)


def vote(request, project_id):
    form = RateProjectForm()
    project = Project.get_project_by_id(project_id)
    
    context = {
        'project': project,
        'form': form
    }
    return render(request, 'vote.html', context)


def rate_project(request, project_id):
    form = RateProjectForm()
    project = Project.get_project_by_id(project_id)
    current_user = request.user

    if request.method == "POST":
        form = RateProjectForm(request.POST)

        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.project = project
            new_rating.user = current_user
            new_rating.save()
            return redirect('home')
    return redirect('home')
