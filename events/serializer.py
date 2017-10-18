from rest_framework import serializers
from .models import Event, Fee, Venue


class EventSerializer(serializers.Serializer):

	class Meta:
		model = Event
		fields = ('id', 'link', 'name', 'description', 'duration', 'rsvp_limit', 'time', 'waitlist_count', 'yes_rsvp_count')


	def create(self, validated_data):
		return Event.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.id = validated_data.get('id', instance.id)
		instance.link = validated_data.get('link', instance.link)
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance


class FeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fee
		fields = ('amount', 'currency')

	# link to event?
	# def create(self, validated_data, event):
	def create(self, validated_data):
		return Fee.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.amount = validated_data.get('amount', instance.id)
		instance.currency = validated_data.get('currency', instance.link)
		instance.save()
		return instance


class VenueSerializer(serializers.ModelSerializer):

	class Meta:
		model = Venue
		fields = ('name', 'lat', 'lon', 'address_1', 'address_2', 'address_3', 'city', 'country', 'state')

	# link to event?
	def create(self, validated_data):
		return Venue.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.event = validated_data.get('event', instance.event)
		instance.name = validated_data.get('name', instance.name)
		instance.lat = validated_data.get('lat', instance.lat)
		instance.lon = validated_data.get('lon', instance.lon)
		instance.address_1 = validated_data.get('address_1', instance.address_1)
		instance.address_2 = validated_data.get('address_2', instance.address_2)
		instance.address_3 = validated_data.get('address_3', instance.address_3)
		instance.city = validated_data.get('city', instance.city)
		instance.country = validated_data.get('country', instance.country)
		instance.state = validated_data.get('state', instance.state)
		instance.save()
		return instance