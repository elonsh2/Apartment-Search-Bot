from bs4 import BeautifulSoup
import requests
from fill_form import FillForm
from brain import GetData


data = GetData()

try:
    form = FillForm(addresses_list=data.get_address(), prices_list=data.get_price(), details_list=data.get_details())
except AttributeError:
    print('Captcha Error')
else:
    print('Completed')
