from __future__ import unicode_literals

from django.test import TestCase, override_settings

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
        pass

    # the method called everytime a test definition is done, think of it as a
    # cleanup method
    def tearDown(self):
        pass

    def test_age(self):
        pass

    def test_unicode(self):
        pass


class EntryModelManagerTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_owned(self):
        pass


class EntryModelTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_unicode(self):
        pass
