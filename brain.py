from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7'
}
APARTMENTS_LINK = 'https://www.yad2.co.il/realestate/rent?topArea=100&area=7&city=3000&price=-1-4000&Order=1&priceOnly=1'


class GetData:
    def __init__(self):
        self.response = requests.get(url=APARTMENTS_LINK, headers=headers)
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
