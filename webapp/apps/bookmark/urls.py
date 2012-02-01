from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'bookmark.views.home', name='home'),
)