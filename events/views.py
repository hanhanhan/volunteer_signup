from django.shortcuts import render
from .models import Event


def home(request):
	context = {}
	events = Event.objects.all()
	context['events'] = events
	return render(request, 'home.html', context=context)
