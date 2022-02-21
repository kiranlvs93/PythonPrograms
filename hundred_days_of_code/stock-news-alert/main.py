from twilio.rest import Client
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_PRICE_API_KEY = "<API_KEY>"
NEWS_API_KEY = "<API_KEY>"
TWILIO_ACC_ID = "<Twilio Acc ID>"
TWILIO_AUTH_TOKEN = "<Twilio Auth Token>"


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
    up_down_symbol = "🔺" if change > 0 else "🔻"
    print(f"{STOCK}: {up_down_symbol}{change}%")
    if abs(change) >= 5:
        get_news()


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
        message_to_be_sent += f"Headline {i + 1}::{article['title']}\n\tBrief::{article['description']}\n"
    print("Sending below message::\n", message_to_be_sent)
    # send_notification(message_to_be_sent)


def send_notification(message):
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = TWILIO_ACC_ID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    # message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',
    #     to='whatsapp:+918095780582'
    # )

    print(message.sid)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
if __name__ == '__main__':
    get_stock_price()
