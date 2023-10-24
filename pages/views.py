from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Team
# Create your views here.


def home(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html', {})


def services(request):
    return render(request, 'pages/services.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})
