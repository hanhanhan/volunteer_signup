from django.test import TestCase
from events.models import Event, Fee, Venue
from events.serializer import EventSerializer, FeeSerializer, VenueSerializer
from rest_framework.parsers import JSONParser
# from settings import BASE_DIR
import json
import os


class EventModelTest(TestCase):

	def setUp(self):
		test_dir = os.path.dirname(__file__)
		file_path = os.path.join(test_dir, 'event_no_fee_no_venue.json')
		with open(file_path, 'rb') as f:
			self.event_no_fee_no_venue = JSONParser().parse(f)

		file_path = os.path.join(test_dir, 'event_with_fee.json')
		with open(file_path, 'rb') as f:
			self.event_with_fee = JSONParser().parse(f)
		
		file_path = os.path.join(test_dir, 'event_with_venue.json')
		with open(file_path, 'rb') as f:
			self.event_with_venue = JSONParser().parse(f)

		

	def test_event_serialization_no_fee_no_venue(self):

		

		# is the documentation's function really better than just json.load? 

		# with open(file_path, 'rb') as f:
		# 	import ipdb; ipdb.set_trace()
		# 	# event_no_fee_no_venue = json.load(f)
		# 	event_no_fee_no_venue = json.load(f)



		event = EventSerializer(data=event_no_fee_no_venue)
		# way to see event.errors()?
		import ipdb; ipdb.set_trace()
		self.assertTrue(event.is_valid())
		event = event.save()
		self.assertIsInstance(event, Event)

	def test_fee_serialization(self):

		file_path = os.path.join(self.test_dir, 'event_with_fee.json')
		with open(file_path) as f:
			event_with_fee = json.load(f)

		fee = FeeSerializer(data=event_with_fee)
		# way to see event.errors()?
		self.assertTrue(fee.is_valid(), msg=f'Serializer error: {fee.errors}')
		fee = fee.save()
		self.assertIsInstance(fee, Fee)

"""
serializers.py
save()
203         validated_data = dict(
204             list(self.validated_data.items()) +
205             list(kwargs.items())
206         )
"""







