from django.shortcuts import render
from allauth.account.decorators import verified_email_required
from .models import Event


def home(request):
	context = {}
	events = Event.objects.all()
	context['events'] = events
	return render(request, 'home.html', context=context)


def event(request):
	pass


@verified_email_required
def volunteer_for(request, event):
	pass
