from app.apis import endpoints
from flask import jsonify, make_response, request
import requests

class Endpoints():

    def __init__(self):
        self.holiday_url = "https://holidays.abstractapi.com/v1/?api_key={}&country={}&year={}&month={}&day={}"

    def obtain_holiday(self, country : str, month : int, day : int, year : int):
        """
        This method will return a json
        :param country: us
        :param month: 12
        :param day: 25
        :param year: 2023
        :return:
           json example:
            [
    {
        "name": "New Year's Day",
        "name_local": "",
        "language": "",
        "description": "",
        "country": "SG",
        "location": "Singapore",
        "type": "National",
        "date": "01/01/2023",
        "date_year": "2023",
        "date_month": "01",
        "date_day": "01",
        "week_day": "Sunday"
        }]
        """
        try:
            api_key = "b15b2bfcfbed45c598a706668f1afd41"
            final_url = self.holiday_url.format(api_key, country, year, month, day, year)
            response = requests.get(url=final_url)
            if response.status_code == 200:
                return response.json()[0]["name"]
            else:
                msg = f"API call failed with error: {response.status_code}"
                raise Exception(msg)
        except:
            msg : "an error ocurred!"
            Exception(msg)

    def get_json(self, final_url):

        response = requests.get(url=final_url)
        return response

