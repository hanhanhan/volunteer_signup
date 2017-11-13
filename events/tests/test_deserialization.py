from django.test import TestCase
from events.models import Event, Fee, Venue

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
		import pdb; pdb.set_trace()

		self.assertIsInstance(event, Event)

	# def test_event_with_fee_serialization(self):
	# 	serializer = EventSerializer(data=self.event_with_fee)
	# 	import pdb; pdb.set_trace()
	# 	self.assertTrue(serializer.is_valid(), msg=f'Event with fee serializer error: {serializer.errors}')
		
	# 	event = serializer.save()
		
	# 	self.assertIsInstance(event, Event)

	# def test_event_with_venue_serialization(self):
	# 	serializer = EventSerializer(data=self.event_with_venue)

	# 	self.assertTrue(serializer.is_valid(), msg=f'Event with venue serializer error: {serializer.errors}')
	# 	event = serializer.save()
	# 	import pdb; pdb.set_trace()
	# 	self.assertIsInstance(event, Event)

	# def test_update_event_no_fee_no_venue(self):
	# 	pass







