from django.shortcuts import redirect, render
from .forms import SubmitProjectForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def submit(request):
    form = SubmitProjectForm()

    if request.method == "POST":
        print('hello')
        return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'submit.html', context)
