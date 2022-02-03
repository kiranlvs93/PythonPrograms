from datetime import datetime as dt
import random
import smtplib
import pandas as pd
from os import listdir
from os.path import isfile, join


def get_quotes():
    """
    Get a quote from the birthdays.csv file
    :return:
    """
    with open("quotes.txt") as inp:
        return random.choice(inp.readlines())


def get_body(user_name):
    """
    Pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    :return:
    """
    files = [f for f in listdir("letter_templates") if isfile(join("letter_templates", f))]
    with open("letter_templates/" + random.choice(files)) as template:
        msg_body = "Subject:Happy Birthday!!! \n\n" + template.read().replace("[NAME]", user_name)
        return msg_body


def send_email(message, to_address):
    """
    Send the letter generated to that person's email address
    :param message:
    :param to_address:
    :return:
    """
    my_email = "__YOUR_EMAIL__"
    password = "__YOUR_PASSWORD__"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)
    print(f"Email sent successfully to {to_address}")


def get_birthday_details(req_month=1, req_day=0):
    """
    Get details of birthday for the given month and day from the birthdays.csv
    :param req_month:
    :param req_day:
    :return:
    """
    birthday_data = pd.read_csv("birthdays.csv")
    mask = (birthday_data.day == req_day) & (birthday_data.month == req_month)
    filtered_data = birthday_data[mask]
    return filtered_data[["name", "email"]]


today = (dt.now().month, dt.now().day)
users_to_be_emailed = get_birthday_details(req_month=today[0], req_day=today[1])
for index, row in users_to_be_emailed.iterrows():
    name = row['name']
    email = row['email']
    body = get_body(name)
    send_email(body, email)
