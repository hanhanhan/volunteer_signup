from django.test import TestCase
from events.models import Event, Fee, Venue
from events.api_event_sync import update_event, get_events_from_api

import json
import os


class EventDeserializationTest(TestCase):

	def setUp(self):
		test_dir = os.path.dirname(__file__)
		file_path = os.path.join(test_dir, 'dummy_data', 'event_with_fee_and_venue.json')

		with open(file_path, 'rb') as f:
			self.api_event = json.load(f)

		file_path = os.path.join(test_dir, 'dummy_data', 'events.json')

		with open(file_path, 'rb') as f:
			self.api_events = json.load(f)


	def test_one_new_event_update_with_fee_and_venue(self):
		# import pdb; pdb.set_trace()
		api_event_id = self.api_event["id"]
		update_event(self.api_event)
		event = Event.objects.all().first()
		fee = Fee.objects.all().first()
		venue = Venue.objects.all().first()

		self.assertEquals(api_event_id, event.meetup_id)
		self.assertEquals(fee.event, event)
		self.assertEquals(venue.event, event)


	def test_get_events_from_api(self):
		api_data = get_events_from_api()
		event_fields = {'id', 'link', 'name', 'description'}
		for field in event_fields:
			self.assertIn(field, api_data[0])


	def test_pull_and_filter_events_from_database(self):
		# db_events = get_upcoming_db_events()
		pass


	def test_sync_with_api(self):
		pass








