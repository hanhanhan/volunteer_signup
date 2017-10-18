from django.conf.urls import url, include
from django.contrib import admin
import events.views as events
import volunteers.views as volunteers

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', events.home, name='home'),
    url(r'profile/(?P<user>\d+)/$', volunteers.user_profile),
    # or
    url(r'profile/$', volunteers.profile),
    url(r'^accounts/', include('allauth.urls')),
]
