from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def info(request):
    return render(request, 'pages/info.html')

def service(request):
    return render(request, 'pages/service.html')

def login(request):
    return render(request, 'pages/login.html')

def error404(request, *args, **kwargs):
    return render(request, 'pages/error404.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})




