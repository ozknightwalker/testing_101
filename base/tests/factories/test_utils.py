from __future__ import unicode_literals

from mock import patch
import httplib as http

from django.test import TestCase

from base.utils import fetchAPI


def mocked_requests_get(*args, **kwargs):
    # overide requests.get
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({"key2": "value2"}, 200)


class FetchAPITestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_request_status_200(self):
        with patch('base.utils.requests.get', side_effect=mocked_requests_get):
            code, response = fetchAPI()
        self.assertEqual(code, http.OK)

    def test_request_status_403(self):
        code, response = fetchAPI()
        self.assertEqual(code, http.FORBIDDEN)
