from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Event


def home(request):
	
	return render(request, 'home.html')


def events(request):
	return render(request, 'events.html')






