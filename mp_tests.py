import unittest
import mp_requests


class TestRequests(unittest.TestCase):

    def test_catalog(self):
        data = mp_requests.get_catalog_request_data()
        respond = mp_requests.get_catalog(data)
        self.assertTrue(respond['Success'])

    def test_category(self):
        pass
        data = mp_requests.get_category_request_data()
        respond = mp_requests.get_category(data)
        self.assertTrue(respond['Success'])

    def test_order_status(self):
        pass
        data = mp_requests.get_order_status_data()
        respond = mp_requests.get_order_status(data)
        self.assertTrue(respond['Success'])


if __name__ == '__main__':
    TestRequests()
