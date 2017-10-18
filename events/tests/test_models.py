from django.test import TestCase
from events.models import Event, Fee, Venue
from events.serializer import EventSerializer, FeeSerializer, VenueSerializer
# from settings import BASE_DIR
import json
import os


class EventModelTest(TestCase):

	def setUp(self):
		self.test_dir = os.path.dirname(__file__)

	def test_event_serialization_no_fee_no_venue(self):

		file_path = os.path.join(self.test_dir, 'event_no_fee_no_venue.json')

		with open(file_path) as f:
			event_no_fee_no_venue = json.load(f)

		event = EventSerializer(data=event_no_fee_no_venue)
		# way to see event.errors()?
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

	







