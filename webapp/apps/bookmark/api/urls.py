from authentication import DjangoAuthentication
from handlers import BookmarkHandler
from django.conf.urls.defaults import patterns, url
from piston.resource import Resource
from piston.doc import documentation_view

auth = DjangoAuthentication()
bookmark_handler = Resource(BookmarkHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^bookmarks/(?P<bookmark_id>\d+)/$', bookmark_handler, name='api_bookmark'),
    url(r'^bookmarks/$', bookmark_handler, name='api_bookmarks'),
)