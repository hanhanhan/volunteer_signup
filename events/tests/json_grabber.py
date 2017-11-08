# generate json for events to consistently test different serialization cases

import json
import requests


def main():
	""" Create json files of different combinations of nested event objects
	for testing.
	"""

	r = requests.get("https://api.meetup.com/Girl-Develop-It-Los-Angeles/events")
	r_json = r.json()

	written_fee_no_venue = False
	written_no_fee_no_venue = False
	written_venue_no_fee = False

	for event in r_json:
		event["event_id"] = event["id"]
		event.pop("id")

		if not written_venue_no_fee and 'venue' in event and 'fee' not in event:
			with open('event_with_venue.json', 'w') as f:
				json.dump(event, f)
			written_venue_no_fee = True

		if not written_fee_no_venue and 'venue' not in event and 'fee' in event:
			with open('event_with_fee.json', 'w') as f:
				json.dump(event, f)
			written_fee_no_venue = True

		if not written_no_fee_no_venue and 'venue' not in event and 'fee' not in event:
			with open('event_no_fee_no_venue.json', 'w') as f:
				json.dump(event, f)
			written_no_fee_no_venue = True

if __name__ == '__main__':
	main()