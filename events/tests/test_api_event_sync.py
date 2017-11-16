from django.test import TestCase
from events.models import Event, Fee, Venue
from events.api_event_sync import update_event

import json
import os


class EventDeserializationTest(TestCase):

	def setUp(self):
		test_dir = os.path.dirname(__file__)
		file_path = os.path.join(test_dir, 'dummy_data', 'event_with_fee_and_venue.json')

		with open(file_path, 'rb') as f:
			self.api_event = json.load(f)

	def test_update_event(self):
		import pdb; pdb.set_trace()
		update_event(self.api_event)
		event = Event.objects.all().first()
		api_id = int(self.api_event["id"])
		self.assertEquals(api_id, event.meetup_id)





