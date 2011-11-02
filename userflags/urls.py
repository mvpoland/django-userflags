from django.conf.urls.defaults import *

from userflags.views import *

# Because you probably want to lock down these kind of views, it is better to decorate the views and
# copy paste this urlconf where appropriate...

# The urlconf below is just an example

urlpatterns = patterns('',
    url(r'^link/(?P<user_id>[0-9]+)/(?P<flag_id>[0-9]+)/$', link, name='userflags_link'),
    url(r'^unlink/(?P<user_id>[0-9]+)/(?P<flag_id>[0-9]+)/$', unlink, name='userflags_unlink'),
)
