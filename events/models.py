from time import time
from django.db import models
from volunteers.models import Volunteer
# NOTE: Add mixin to log issues saving
# https://stackoverflow.com/questions/38041310/log-all-save-update-delete-actions-in-all-django-models

class Event(models.Model):
	# NOTE: id is alphanumeric unique identifier per meetup API, not necessarily integer
	meetup_id = models.IntegerField(unique=True)
	link = models.URLField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.TextField(default='')
	duration = models.PositiveIntegerField(null=True)
	rsvp_limit = models.SmallIntegerField(null=True)
	# event start time in milliseconds since epoch
	time = models.BigIntegerField(null=True) 
	waitlist_count = models.BigIntegerField(null=True)
	yes_rsvp_count = models.SmallIntegerField(null=True)
	volunteers_requested = models.SmallIntegerField(null=True)
	volunters_signedup = models.SmallIntegerField(default=0)
	volunteer_skills_desc = models.TextField(default='')
	local_date = models.CharField(max_length=20, default='')
	local_time = models.CharField(max_length=20, default='')
	updated = models.PositiveIntegerField(null=True)
	utc_offset = models.PositiveIntegerField(null=True)	

	def __str__(self):
		return self.name


class Fee(models.Model):
	event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
	amount = models.IntegerField(null=True)
	currency = models.CharField(max_length=10, default='')


class Venue(models.Model):
	event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=200)
	lat = models.DecimalField(decimal_places=20, max_digits=25)
	lon = models.DecimalField(decimal_places=20, max_digits=25)
	address_1 = models.CharField(max_length=200, default='')
	address_2 = models.CharField(max_length=200, default='')
	address_3 = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=50, default='')
	country = models.CharField(max_length=50, default='')
	state = models.CharField(max_length=50, default='')


class Event_Volunteer(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, primary_key=True)
	volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	showed = models.BooleanField()
	signup_date = models.DateTimeField(auto_now_add=True)
	cancel_date = models.DateTimeField(null=True)

