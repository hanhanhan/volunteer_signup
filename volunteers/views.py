from django.shortcuts import render


def user_profile(request, user):
	return render(request, template_name='profile.html')


def profile(request):
	if request.user.is_anonymous:
		# return redirect()
		return
	else:
		return render(request, template_name='profile.html')
