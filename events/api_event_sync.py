import json
import logging
import os
import requests
from time import time

from .models import Event, Fee, Venue

JSON_FILE = 'events.json'
URL = "https://api.meetup.com/Girl-Develop-It-Los-Angeles/events?&status=upcoming"

# QUESTION: Implement as class properties?
EVENT_FIELDS = {field.name for field in Event._meta.get_fields()}
FEE_FIELDS = {field.name for field in Fee._meta.get_fields()}
VENUE_FIELDS = {field.name for field in Venue._meta.get_fields()}

logger = logging.getLogger(__name__)


def get_event_data():
	r = requests.get(URL)
	with open(JSON_FILE, 'w') as f:
		json.dump(r.json(), f)


# QUESTION: How do I rearrange this so I can fake data in tests?
def get_events_from_api():
	if not os.path.exists(JSON_FILE):
		get_event_data()

	with open('events.json', 'rb') as f:
		events = json.load(f)
		return events


def get_upcoming_db_events():
	millisecs = time() * 1000
	events = Event.objects.all().filter(time__gt=millisecs)
	return events


def get_modified_events(api_events, db_events):
	db_events = {(event.event_id, event.updated) for event in db_events}
	api_events = {(event["id"], event["updated"]) for event in api_events}

	modified_events = {event[0] for event in (api_events - db_events)}
	return modified_events


def get_new_events(api_events, db_events):
	db_event_ids = {event.event_id for event in db_events}
	api_event_ids = {event["id"] for event in api_events}
	new_events = api_event_ids - db_event_ids
	return new_events


def update_event(api_event):
	""" Create event in database from dictionary pulled from Meetup API. No return value.
	"""
	try:
		event = Event.objects.get(event_id=api_event["id"])
	except Event.DoesNotExist:
		event = Event()

	if "venue" in api_event:
		# get intersection of fields in Venue model and values for "venue" from API
		try:
			venue = Venue.objects.get(event=event)
		except:
			venue = Venue()

		filtered_api = {k: v for k, v in api_event["venue"] if k in VENUE_FIELDS}
		filtered_api["event"] = event

		for k, v in filtered_api:
			setattr(venue, k, v)

		api_event.pop("venue")

	if "fee" in api_event:
		# NOTE: duplicate from above. DRY -> turn into function?
		filtered_api = {k: v for k, v in api_event["fee"] if k in FEE_FIELDS}
		filtered_api["event"] = event
		try:
			fee = Fee.objects.get(event=event)
		except Fee.DoesNotExist:
			fee = Fee()

		for k, v in filtered_api:
			setattr(fee, k, v)

		api_event.pop("fee")

	# Replace python keyword from dictionary.
	api_event["event_id"] = api_event["id"]

	for key in api_event:
		filtered_api = {k: v for k, v in api_event if k in EVENT_FIELDS}

	for key, value in filtered_api.items():
		setattr(event, key, value)

	event.save()

	if venue:
		venue.save()
	if fee:
		fee.save()


def sync_with_api():
	""" Get events from meetup API. Save/update events them in the database if they don't match API values. No return value.
	"""
	api_events = get_events_from_api()
	db_events = get_upcoming_db_events()
	# QUESTION: Better name for updated + new? handle together?
	modified_events = get_modified_events(api_events, db_events)
	# QUESTION: could I use map here? it's lazy and I don't need return value, so I'm not sure how to make it evaluate
	for event in new_events:
		create_event(event)

	for event in updated_events:
		update_event(event)


if __name__ == '__main__':
	sync_with_api()