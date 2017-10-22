from __future__ import unicode_literals

import httplib as http

from django.test import TestCase
from django.core.urlresolvers import reverse


class HomepageViewTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_method(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_post_method(self):
        response = self.client.post(reverse('homepage'))
        self.assertEqual(response.status_code, http.METHOD_NOT_ALLOWED)
