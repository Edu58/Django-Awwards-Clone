from django.shortcuts import get_object_or_404, redirect, render
from .forms import RateProjectForm, SubmitProjectForm
from .models import Profile, Project, Rating
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm


def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html', {'form': form})


def index(request):
    return render(request, 'index.html')

def home(request):
    all_projects = Project.objects.all()

    if request.method == "POST":
        query = request.POST.get('project-query')
        results = Project.get_project_by_title(query)
        
        context = {
            'projects': results,
        }

        return render(request, 'home.html', context)

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

    if request.method == "POST":
        form = RateProjectForm(request.POST)
        current_user = request.user
        
        if form.is_valid():
            check_if_voted = Rating.objects.filter(user=current_user).exists()

            if not check_if_voted:
                project = Project.get_project_by_id(project_id)

                new_rating = form.save(commit=False)
                new_rating.project = project
                new_rating.user = current_user
                new_rating.save()
                return redirect(reverse('vote', args=[project_id]))

            return redirect(reverse('vote', args=[project_id]))
            
    return redirect('home')


def profile(request, username):
    return render(request, 'profile.html')