import requests
import json
import os

SHEETY_API_KEY = os.getenv("FF_SHEETY_API_KEY")
SHEETY_AUTH = os.getenv("FF_SHEETY_AUTH")
URL = "https://api.sheety.co/{sheety_api_key}/flightDeals/{sheet_name}"
HEADERS = {"Authorization": SHEETY_AUTH, "Content-Type": "application/json"}


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """

    def __init__(self, sheet_name):
        """
        Read the entire sheet data
        :param sheet_name:
        """
        self.sheet_name = sheet_name
        self.url = URL.format(sheety_api_key=SHEETY_API_KEY, sheet_name=self.sheet_name)
        self.sheet_data = self.read_sheet()

    def read_sheet(self):
        print(f"Reading sheet {self.sheet_name}")
        response = requests.get(url=self.url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
        # with open("prices_sheet_response.json") as sheet:
        #     return json.load(sheet)

    def add_row(self, params):
        """
        Add a row to the sheet
        :param params:
        :return:
        """
        print("Adding row to the sheet")
        requests.post(url=self.url, headers=HEADERS, json=params)

    def update_row(self, params, row_num):
        """
        Update an existing row
        :param row_num:
        :param params:
        :return:
        """
        print(f"Updating row no {row_num} in the sheet....")
        response = requests.put(url=self.url + f"/{row_num}", headers=HEADERS, json=params)
        response.raise_for_status()
        print("Update successful")
        print("**********************")
