from selenium import webdriver
import time
from os import environ


class FillForm:
    def __init__(self, addresses_list: list, prices_list: list, details_list: list):
        self.driver = webdriver.Chrome(executable_path=environ['CHROME_DRIVER_PATH'])
        self.driver.get(environ['FORMS_LINK'])
        time.sleep(0.2)
        try:
            for item in range(len(addresses_list)):
                self.fill_form(addresses_list[item], prices_list[item], details_list[item])
        except IndexError:
            self.driver.quit()
            return

    def fill_form(self, address, price, details):
        inputs = self.driver.find_elements_by_css_selector('.quantumWizTextinputPaperinputInput.exportInput')
        inputs[0].send_keys(address)
        inputs[1].send_keys(price)
        inputs[2].send_keys(details)
        submit_button = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()
        time.sleep(0.1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()





