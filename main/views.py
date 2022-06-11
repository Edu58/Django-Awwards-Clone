from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def submit(request):
    return render(request, 'submit.html')
