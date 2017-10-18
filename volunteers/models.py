from django.db import models
from django.contrib.auth.models import AbstractUser
# from events.models import Event, Event_Volunteer


class Volunteer(AbstractUser):
	USERNAME_FIELD = 'username'
	interests = models.TextField(blank=True)
	logged_hours = models.PositiveSmallIntegerField(default=0)
	redeemed_hours = models.PositiveSmallIntegerField(default=0)
	events = models.ManyToManyField(
        'events.Event',
        through='events.Event_Volunteer',
        # through_fields=('name', 'id', 'time'), # this doesn't mean what I thougt it means
    )