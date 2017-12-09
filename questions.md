# For Codementor 12/5/17

Caution - putting github/fb apps in db for allauth, and putting db in git, and app in github...

Fixtures?

Django testrunner w/selenium function tests?
Name my functional test functional_test? test_functional? folder?
leverage allauth tests?
https://github.com/pennersr/django-allauth/blob/master/allauth/account/tests.py

So many ways to do it.....LiveServerTestCase/Static+django test runner (location to run from	?), unittest and no django test runner

Getting it working FB, GitHub login

Am I commenting the right way to be able to generate documentation later?

Outline next steps

-managment command for scheduling asking cron job




# allauth site?
In django admin, it says:
Add a Site for your domain, matching settings.SITE_ID (django.contrib.sites app). 
Can I use localhost? Made up name? How is this used?

https://developers.facebook.com/apps/1483671008393141/dashboard/

URL Blocked: This redirect failed because the redirect URI is not whitelisted in the app’s Client OAuth Settings. Make sure Client and Web OAuth Login are on and add all your app domains as Valid OAuth Redirect URIs.

https://developers.facebook.com/apps/1483671008393141/dashboard/




https://github.com/settings/applications/603836

# How to mix custom templates + default?
How can I use allauth's (or django's) templates with my own base template, styling?

# what should I use between github + facebook accounts to display profile, url capture group?

# login redirects to accounts/login or accounts/profile -- how should I define url? redefine url? does it mess things up if I define profile/ instead

# how do I configure facebook, github for testing from localhost?

# post request to profile -- request.POST.get('user') instea of get w/url?
if its a post request how do i wire up references to it?
or -- user is already know since logged in -- just access in template

# why does the signup page exist but not login???? where is magic happening?

# Many to many fields
https://docs.djangoproject.com/en/1.11/topics/db/models/#intermediary-manytomany
Your intermediate model must contain one - and only one - foreign key to the source model - does it matter which?

# is my many to many table ok? urg circular imports


<!--  -->
nested json
better ways to figure stuff out


customize default templates

---
python manage.py test
python manage.py test functional_tests
----
shortcut to see json nice in sublime prettyjson
ipdb
jump to definition
api star
sublime snippets
python slack
var(x) instead of dir(x)

me@me.com
developit

eleanor
pw: roosevelt