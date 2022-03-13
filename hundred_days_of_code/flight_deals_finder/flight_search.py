import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
FLIGHT_SEARCH_API_KEY = os.getenv("FF_TEQUILA_API")
HEADERS = {"apikey": FLIGHT_SEARCH_API_KEY}


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API
    """

    def get_iata_code(self, city_name):
        location_search_url = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"locale": "en-US", "location_types": "city", "limit": "10",
                 "active_only": "true", "term": city_name}
        response = requests.get(url=location_search_url, headers=HEADERS, params=query)
        response.raise_for_status()
        response = response.json()["locations"]
        for location in response:
            if location["name"].lower() == city_name.lower():
                print(f"Found IATA code for {city_name}:: {location['code']}")
                return location['code']

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
            "sort": "price",#duration, quality,date
            "asc": 1
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=HEADERS,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: Rs.{flight_data.price}")
        return flight_data
