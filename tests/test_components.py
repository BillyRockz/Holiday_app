"""Test for components models"""

from unittest import mock, TestCase
from app.views.components import Endpoints

class TestEndpoints(TestCase):

    @mock.patch("requests.get")
    def test_01_components_success(self, m_get):
        m_get.return_value.status_code = 200
        m_get.return_value.json.return_value = [{"name":"Saint Patrick Day"}]
        day = "25"
        month = "12"
        year = "2023"
        country = "us"
        response = Endpoints().obtain_holiday_name(country=country, month=month, day=day, year=year)
        self.assertEqual("Saint Patrick Day", response)\

    @mock.patch("requests.get")
    def test_01_components_failure(self, m_get):
        m_get.return_value.status_code = 404
        m_get.return_value.json.return_value = ""
        day = "25"
        month = "abc"
        year = "2023"
        country = "us"
        response = Endpoints().obtain_holiday_name(country=country, month=month, day=day, year=year)
        self.assertEqual(None, response)

