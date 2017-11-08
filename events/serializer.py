from rest_framework import serializers
from .models import Event, Fee, Venue


class FeeSerializer(serializers.ModelSerializer):
	event = serializers.PrimaryKeyRelatedField()
	# event = serializers.OneToOneField()

	class Meta:
		model = Fee
		fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
	# event = serializers.OneToOneField()
	event = serializers.PrimaryKeyRelatedField()

	class Meta:
		model = Venue
		fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
	fee = FeeSerializer(required=False)
	venue = VenueSerializer(required=False)

	class Meta:
		model = Event
		fields = '__all__'

	def create(self, validated_data):
		fee, venue = False, False
		import pdb; pdb.set_trace()

		if 'fee' in validated_data.keys():
			fee_data = validated_data.pop('fee')
			# fee_data = validated_data['fee']
			fee = True

		if 'venue' in validated_data.keys():
			venue_data = validated_data.pop('venue')
			# venue_data = validated_data['venue']
			venue = True

		event = Event.objects.create(**validated_data)

		if fee:
			Fee.objects.create(event=event, **fee_data)

		if venue:
			Venue.objects.create(event=event, **venue_data)

		return event


	# def update(self, instance, validated_data):
		# pass