import unittest
from unittest import mock
from main import get_all_stats_name


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://pokeapi.co/api/v2/stat/":
        return MockResponse(
            {
                "results": [
                    {"name": "hp"},
                    {"name": "attack"},
                    {"name": "defense"},
                    {"name": "special-attack"},
                    {"name": "special-defense"},
                    {"name": "speed"},
                    {"name": "accuracy"},
                    {"name": "evasion"},
                ],
            },
            200,
        )


class TestIntegration(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_getting_all_stat_name(self, mock_request):
        stat_names = get_all_stats_name()
        self.assertEqual(
            stat_names,
            [
                "hp",
                "attack",
                "defense",
                "special-attack",
                "special-defense",
                "speed",
                "accuracy",
                "evasion",
            ],
        )

    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_convert_json_to_pokemon(self, mock_request):
        pass
