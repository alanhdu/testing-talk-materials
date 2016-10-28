import requests_mock

from ..integration import num_courses


def test_num_courses():
    with requests_mock.mock() as mock:
        url = "http://api.test"
        mock.get(url, text='{"courses": []}')

        assert num_courses(url) == 0
