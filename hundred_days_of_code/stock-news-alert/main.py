from twilio.rest import Client
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API_KEY = "<API_KEY>"
NEWS_API_KEY = "<API_KEY>"
TWILIO_ACC_ID = "<Twilio Acc ID>"
TWILIO_AUTH_TOKEN = "<Twilio Auth Token>"
TWILO_NUMBER = "<Twilio_Number>"
TO_NUMBER = "<To_Number>"


def get_stock_price():
    """
    Use https://www.alphavantage.co to get the stock price
    When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    :return:
    """
    stock_price_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_PRICE_API_KEY}"
    response = requests.get(stock_price_url)
    response.raise_for_status()
    response_json = response.json()["Time Series (Daily)"]
    # get the price of the last two days
    price_yest = 200  # response_json.pop(list(response_json.keys())[0])["4. close"]
    price_day_before = 100  # response_json.pop(list(response_json.keys())[0])["4. close"]
    change = ((float(price_yest) - float(price_day_before)) / float(price_day_before)) * 100
    return change


def get_news():
    """
    Get the first 3 news pieces for the COMPANY_NAME
    :return:
    """
    parameter = {"pageSize": 3, "apiKey": NEWS_API_KEY, "q": COMPANY_NAME}
    news_api = f"https://newsapi.org/v2/everything"
    response = requests.get(url=news_api, params=parameter)
    response.raise_for_status()
    articles = response.json()["articles"]
    message_to_be_sent = ""
    for i, article in enumerate(articles):
        message_to_be_sent += f"Headline {i + 1}::{article['title']}\n\tBrief::{article['description']}\n\n"
    print("Sending below message::\n", message_to_be_sent)
    return message_to_be_sent


def send_notification(notification):
    """
    Use https://www.twilio.com to send message
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    :param notification:
    :return:
    """
    account_sid = TWILIO_ACC_ID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=('whatsapp:%s' % TWILO_NUMBER),
        body=notification,
        to=('whatsapp:%s' % TO_NUMBER)
    )

    print(message.sid)


if __name__ == '__main__':
    notification_message = ""
    price_change = get_stock_price()
    up_down_symbol = "🔺" if price_change > 0 else "🔻"
    notification_message = f"{STOCK}: {up_down_symbol}{price_change}%\n\n"
    if abs(price_change) >= 5:
        notification_message += get_news()
        send_notification(notification_message)
