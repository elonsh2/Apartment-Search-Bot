from bs4 import BeautifulSoup
import requests
from os import environ
HEADERS = {
    'User-Agent': environ['OWN_USER_AGENT'],
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.google.com/',
    'Host': 'www.yad2.co.il',
    "Connection": "keep-alive",
    'cookie': environ['OWN_COOKIE_HEADER']


}
APARTMENTS_LINK = 'https://www.yad2.co.il/realestate/rent?topArea=100&area=7&city=3000&price=-1-4000&Order=1&priceOnly=1'


class GetData:
    def __init__(self):
        self.response = requests.get(url=APARTMENTS_LINK, headers=HEADERS)
        self.web_page = self.response.text
        self.soup = BeautifulSoup(self.web_page, 'html.parser')
        self.feed_list = self.soup.find(class_='feed_list')
        self.addresses = []
        self.prices = []
        self.details = []

    def get_address(self):
        addresses_raw = self.feed_list.find_all(class_='title')
        for item in addresses_raw:
            self.addresses.append(item.getText().strip())
        return self.addresses

    def get_price(self):
        prices_raw = self.feed_list.find_all(class_='price')
        for item in prices_raw:
            self.prices.append(item.getText().strip())
        return self.prices

    def get_details(self):
        details_raw = self.feed_list.find_all(class_='subtitle')
        for item in details_raw:
            self.details.append(item.getText().strip())
        return self.details
