from __future__ import unicode_literals

# from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.utils import timezone

from base.models import Profile, Entry
from base.tests.factories.profile import ProfileFactory
from base.tests.factories.user import UserFactory
from base.tests.factories.entry import EntryFactory

# if you want to override something from the settings.py you can use the
# override_settings decorator to do so
# by:

# @override_settings(DEBUG=True)
# class TestClass(TestCase):

# or
# class TestCase(TestCase):

#     @override_settings(DEBUG=True):
#     def test_something(self):
#         pass


# we usually use the model name + TestCase to create a testcase of a model
class ProfileModelTestCase(TestCase):

    # runs once per TestCase, usually used to initialize constants or loading
    # this initial data for the testcase
    @classmethod
    def setUpTestData(self):
        pass

    # the method called first before running a test, think of it like a
    # constructor
    def setUp(self):
        # self.user = User.objects.create_user(username='test', password='test')
        # self.profile = Profile.objects.create(owner=self.user)
        self.profile = ProfileFactory(full_name='')

    # the method called everytime a test definition is done, think of it as a
    # cleanup method
    def tearDown(self):
        pass

    def test_age(self):
        expected = None
        time = timezone.now()
        self.assertEquals(self.profile.age, expected)
        expected = 25  # years
        days = (expected + 1) * 356
        self.profile.birthdate = time - timezone.timedelta(days=days)
        self.profile.save()
        self.assertEqual(self.profile.age, expected)

    def test_unicode(self):
        expected = '\'s profile'.format(self.profile.full_name)
        self.assertEquals(self.profile.__unicode__(), expected)
        self.profile.full_name = 'Test'
        expected = '{0}\'s profile'.format(self.profile.full_name)
        self.assertEquals(self.profile.__unicode__(), expected)


class EntryModelManagerTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def create_entries(self, range):
        # for x in xrange(range):
        #     Entry.objects.create(owner=self.user, title='testing-{}'.format(x))
        EntryFactory.create_batch(range, owner=self.user)

    def tearDown(self):
        pass

    def test_owned(self):
        expected = 0
        self.assertEquals(
            Entry.objects.owned(owner=self.user).count(), expected)
        expected = 9
        self.create_entries(expected)
        self.assertEquals(
            Entry.objects.owned(owner=self.user).count(), expected)


class EntryModelTestCase(TestCase):

    def setUp(self):
        # self.user = User.objects.create_user(username='test', password='test')
        # self.entry = Entry.objects.create(owner=self.user, title='testing')
        self.title = 'testing'
        self.entry = EntryFactory(title=self.title)
        self.user = self.entry.owner

    def tearDown(self):
        pass

    def test_unicode(self):
        expected = '{0} - {1}'.format(self.title, self.user)
        self.assertEquals(self.entry.__unicode__(), expected)
