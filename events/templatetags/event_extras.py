from django import template

register = template.Library()


@register.filter(name='epoch_to_datetime',)
def event_time(event):
	from time import gmtime
	from datetime import datetime
	# time + utc_offset
	gmt_time = event.time / 1000
	# offset = event.offset / 1000
	offset = 0
	time_tuple = gmtime(gmt_time + offset)
	return time_tuple
	# datetime.datetime(*structTime[:6])
	# return datetime.fromtimestamp(time_tuple)
