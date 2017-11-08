from rest_framework import serializers
from .models import Event, Fee, Venue


class FeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fee
		fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):

	class Meta:
		model = Venue
		fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

	class Meta:
		model = Event
		# event_id = serializers.IntegerField(source='id')
		fee = FeeSerializer(required=False)
		venue = VenueSerializer(required=False)
		fields = '__all__'

	def create(self, validated_data):
		fee, venue = False, False
		import pdb; pdb.set_trace()

		if 'fee' in validated_data.keys():
			fee_data = validated_data.pop('fee')
			fee = True

		if 'venue' in validated_data.keys():
			venue_data = validated_data.pop('venue')
			venue = True

		event = Event.objects.create(**validated_data)

		if fee:
			Fee.objects.create(event=event, **fee_data)

		if venue:
			Venue.objects.create(event=event, **venue_data)

		return event


	# def update(self, instance, validated_data):
	# 	instance.id = validated_data.get('id', instance.id)
	# 	instance.link = validated_data.get('link', instance.link)
	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.description = validated_data.get('description', instance.description)
	# 	instance.save()
	# 	return instance

# EventSerializer._declared_fields['event_id'] = EventSerializer._declared_fields['id']
# del EventSerializer._declared_fields['id']