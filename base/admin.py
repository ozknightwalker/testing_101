from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile, Entry


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    raw_id_fields = ('owner',)


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    raw_id_fields = ('owner',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Entry, EntryAdmin)
