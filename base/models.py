from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    birthdate = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=150, blank=True)
    when = models.DateTimeField(auto_now_add=True)

    @property
    def age(self):
        if not self.birthdate:
            return None

        today = date.today()
        return (today.year - self.birthdate.year -
                ((today.month, today.day) <
                 (self.birthdate.month, self.birthdate.day)))

    def __unicode__(self):
        return '{0}\'s profile'.format(self.full_name)

    class Meta:
        ordering = ['pk']


class EntryModelManager(models.Manager):

    def owned(self, owner):
        return Entry.objects.filter(owner=owner)


class Entry(models.Model):
    owner = models.ForeignKey(User, related_name='entries')
    title = models.TextField(null=False, blank=False)
    when = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='/media/video/',
                             max_length=256, blank=True)
    # sample custom model manager
    objects = EntryModelManager()

    def __unicode__(self):
        return '{0} - {1}'.format(self.title, self.owner)

    class Meta:
        ordering = ['pk']
        verbose_name_plural = 'entries'
