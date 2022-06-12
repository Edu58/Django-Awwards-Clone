from django.shortcuts import get_object_or_404, redirect, render
from .forms import RateProjectForm, SubmitProjectForm, SignUpForm, UpdateProfileForm, UserUpdateForm
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm


def signup_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'signup.html', {'form': form})

def login_user(request):
    form = LoginUserForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html', {'form': form})


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def vote(request, project_id):
    form = RateProjectForm()
    project = Project.get_project_by_id(project_id)
    
    context = {
        'project': project,
        'form': form
    }
    return render(request, 'vote.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def profile(request, username):
    user = get_object_or_404(User, username=username)

    can_update = False

    if request.user == user:
        can_update = True
    else:
        can_update = False

    context = {
        'user':user,
        'can_update': can_update
    }
    return render(request, 'profile.html', context)


@login_required(login_url='login')
def update_profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('profile', args=[request.user]))
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'prof_form': profile_form
    }

    return render(request, 'update-profile.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
