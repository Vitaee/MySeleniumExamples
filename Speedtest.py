from selenium import webdriver
from time import time 

class Speed:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def pressButon(self):
        self.browser.get("https://www.speedtest.net/")
        time.sleep(2)
        butonPress = self.browser.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[2]/div[3]/div[1]/a")
        butonPress.click()
        time.sleep(2)

sped = Speed()
sped.pressButon()
