import os
import requests
from datetime import datetime as dt, timedelta

LOCATION_SEARCH_URL = "https://tequila-api.kiwi.com/locations/query?locale=en-US&location_types=city&limit=10" \
                      "&active_only=true&term={CITY}"
FLIGHT_SEARCH_API_KEY = os.getenv("FF_TEQUILA_API")
HEADERS = {"apikey": FLIGHT_SEARCH_API_KEY}

today = dt.today().date()
from_date = today + timedelta(days=1)
to_date = today + timedelta(weeks=6 * 4)


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API
    """

    def get_iata_code(self, city_name):
        response = requests.get(url=LOCATION_SEARCH_URL.format(CITY=city_name), headers=HEADERS)
        response.raise_for_status()
        response = response.json()
        for location in response["locations"]:
            if location["name"].lower() == city_name.lower():
                print(f"Found IATA code for {city_name}:: {location['code']}")
                return location['code']

    def find_flight(self, from_city_code, to_city_code):
        """

        :param from_city_code:
        :param to_city_code:
        :return:
        """
        pass
