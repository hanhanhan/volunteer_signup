from django.db import models
from volunteers.models import Volunteer


class Event(models.Model):
	# these are the fields of interest from the Meetup API events endpoint
	# id is alphanumeric unique identifier per meetup API, not necessarily integer
	# bad idea to use id keyword? if changed, serializer needs customization
	id = models.IntegerField(primary_key=True)
	link = models.URLField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.TextField(default='')
	duration = models.PositiveIntegerField(null=True)
	rsvp_limit = models.SmallIntegerField(null=True)
	time = models.BigIntegerField(null=True)
	waitlist_count = models.BigIntegerField(null=True)
	yes_rsvp_count = models.SmallIntegerField(null=True)
	volunteers_requested = models.SmallIntegerField(null=True)
	volunters_signedup = models.SmallIntegerField(default=0)
	volunteer_skills_desc = models.TextField(default='')

	# volunteers = models.ManyToManyField(
 #        'volunteers.Volunteer',
 #        through='Event_Volunteer',
 #        through_fields=('username'),
 #    )


	def __str__(self):
		return self.name


class Fee(models.Model):
	event = models.OneToOneField(to=Event, on_delete=models.CASCADE, primary_key=True, related_name='fee')
	amount = models.IntegerField(null=True)
	currency = models.CharField(max_length=10, default='')


class Venue(models.Model):
	event = models.OneToOneField(to=Event, on_delete=models.CASCADE, primary_key=True, related_name='venue')
	name = models.CharField(max_length=200)
	lat = models.DecimalField(decimal_places=14, max_digits=17)
	lon = models.DecimalField(decimal_places=14, max_digits=17)
	address_1 = models.CharField(max_length=200, default='')
	address_2 = models.CharField(max_length=200, default='')
	address_3 = models.CharField(max_length=200, default='')
	city = models.CharField(max_length=50, default='')
	country = models.CharField(max_length=50, default='')
	state = models.CharField(max_length=50, default='')


class Event_Volunteer(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
	showed = models.BooleanField()
	signup_date = models.DateTimeField(auto_now_add=True)
	cancel_date = models.DateTimeField(null=True)

