from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

class Bookmark(models.Model):
    owner = models.ForeignKey(User, verbose_name=_(u'Owner'), related_name='owner_bookmarks')
    favorite_users = models.ManyToManyField(User, verbose_name=_(u'Favorite users'), related_name='favorite_bookmarks',
        blank=True)
    title = models.CharField(verbose_name=_(u'Title'), max_length=100, help_text=_(u'Limit of 100 characters'))
    url = models.URLField(verbose_name=_(u'URL'))
    tags = TaggableManager(verbose_name=_(u'Tags'), blank=True,
        help_text=_(u'A comma-separated list of tags. At most 3.'))
    public = models.BooleanField(verbose_name=_(u'Public this bookmark'), default=True)
    screenshot = models.ImageField(verbose_name=_(u'Screenshot'), upload_to='bookmark', blank=True)
    create_time = models.DateTimeField(verbose_name=_(u'Create time'), auto_now_add=True)

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['-create_time']
        app_label = 'bookmark'