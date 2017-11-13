from django.db import models
from django.contrib.auth.models import AbstractUser
# from events.models import Event, Event_Volunteer


class Volunteer(AbstractUser):
	USERNAME_FIELD = 'username'
	interests = models.TextField(blank=True)
	logged_hours = models.PositiveSmallIntegerField(default=0)
	redeemed_hours = models.PositiveSmallIntegerField(default=0)

