from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User

from base.models import Profile


class CreateProfileSignalTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_profile_when_user_is_created(self):
        user = User.objects.create_user(username='testing', password='testing')
        self.assertNotEquals(Profile.objects.filter(owner=user), [])
