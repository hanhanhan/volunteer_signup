from django.shortcuts import render


def home(request):
	context = {'events': [1, 3, 7]}
	return render(request, template_name='home.html', context=context)

def login(request):
	return render(request, template='login.html')
