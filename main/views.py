from django.shortcuts import get_object_or_404, redirect, render
from .forms import SubmitProjectForm
from .models import Profile, Project, Rating

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
    project = get_object_or_404(Project, pk=project_id)

    

    return render(request, 'vote.html')