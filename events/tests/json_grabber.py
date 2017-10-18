# generate json for events to consistently test different serialization cases

import json
import requests


def main():
	r = requests.get("https://api.meetup.com/Girl-Develop-It-Los-Angeles/events")
	r_json = r.json()

	for event in r_json:
		if 'venue' in event and 'fee' not in event:
			with open('event_with_venue.json', 'w') as f:
				json.dump(event, f)
			break

	for event in r_json:
		if 'venue' not in event and 'fee' in event:
			with open('event_with_fee.json', 'w') as f:
				json.dump(event, f)
			break

	for event in r_json:
		if 'venue' not in event and 'fee' not in event:
			with open('event_no_fee_no_venue.json', 'w') as f:
				json.dump(event, f)
			break

if __name__ == '__main__':
	main()