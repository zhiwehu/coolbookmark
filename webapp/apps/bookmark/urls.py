from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.home', name='bookmarks'),
)