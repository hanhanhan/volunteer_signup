from django.test import TestCase
from events.models import Event, Fee, Venue
from events.serializer import EventSerializer, FeeSerializer, VenueSerializer
from rest_framework.parsers import JSONParser
# from settings import BASE_DIR
import json
import os


class EventDeserializationTest(TestCase):

	def setUp(self):
		test_dir = os.path.dirname(__file__)
		file_path = os.path.join(test_dir, 'event_no_fee_no_venue.json')

		# QUESTION: is the REST Framework jsonparser function preferable to json.load? 
		with open(file_path, 'rb') as f:
			self.event_no_fee_no_venue = JSONParser().parse(f)

		file_path = os.path.join(test_dir, 'event_with_fee.json')
		with open(file_path, 'rb') as f:
			self.event_with_fee = JSONParser().parse(f)

		file_path = os.path.join(test_dir, 'event_with_venue.json')
		with open(file_path, 'rb') as f:
			self.event_with_venue = JSONParser().parse(f)

	def test_event_serialization_no_fee_no_venue(self):
		event = EventSerializer(data=self.event_no_fee_no_venue)
		# way to see event.errors()?
		self.assertTrue(event.is_valid(), msg=f'Serializer error: {event.errors}')
		event = event.save()
		self.assertIsInstance(event, Event)

	def test_fee_serialization(self):
		fee = FeeSerializer(data=event_with_fee)
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







