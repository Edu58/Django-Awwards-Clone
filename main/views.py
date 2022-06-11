from django.shortcuts import redirect, render
from .forms import SubmitProjectForm
from .models import Profile, Project, Rating

# Create your views here.
def index(request):
    all_projects = Project.objects.all()
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

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
