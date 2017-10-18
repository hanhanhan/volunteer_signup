import logging
import requests
from .serializer import EventSerializer, FeeSerializer, VenueSerializer
from .models import Event, Fee, Venue


URL = "https://api.meetup.com/Girl-Develop-It-Los-Angeles/events"
logger = logging.getLogger(__name__)


def sync_events():
	r = requests.get(URL)
	json = r.json()
	for event_json in json:
		event_serializer = EventSerializer(data=event_json)

		# check if it's in the database to know whether to call save() with event object for update

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