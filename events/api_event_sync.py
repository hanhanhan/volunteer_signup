import json
import logging
import os
import requests
from .serializer import EventSerializer, FeeSerializer, VenueSerializer


JSON_FILE = 'events.json'
URL = "https://api.meetup.com/Girl-Develop-It-Los-Angeles/events"
logger = logging.getLogger(__name__)


def get_event_data():
	r = requests.get(URL)
	with open(JSON_FILE, 'w') as f:
		json.dump(r.json(), f)


def sync_events():
	if not os.path.exists(JSON_FILE):
		get_event_data()

	with open('events.json', 'rb') as f:
		events_json = json.load(f)

	for event_json in events_json:
		event_serializer = EventSerializer(data=event_json)

		if event_serializer.is_valid():
			event = event_serializer.save()
		else:
			logging.error(f'Event with invalid data could not be saved: {event_serializer.errors}')
			break

		# I know this should be DRYed and error-proofed but not sure how to go about it
		if 'venue' in event_json:
			venue_serializer = VenueSerializer(data=event_json['venue'])
			venue_serializer.initial_data['event'] = event.id
			if venue_serializer.is_valid():
				venue_serializer.save()

		if 'fee' in event_json:
			fee_serializer = FeeSerializer(data=event_json['fee'])
			fee_serializer.initial_data['event'] = event.id
			if fee_serializer.is_valid():
				fee_serializer.save()


if __name__ == '__main__':
	sync_events()