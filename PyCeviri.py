#gitname = "Vitaee"
#gitpass = "can_aassff88"

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

class Ceviri:
    def __init__ (self):
        self.browser = webdriver.Chrome()
    def transWord(self):
        self.browser.get("https://translate.google.com/?hl=tr")
        time.sleep(2)
        wordTrans = self.browser.find_element_by_xpath("//*[@id='source']")
        wordTrans.send_keys("Moreover, as time goes by, businesses have recognized the importance of the acquisition of new data than creation from at least existing information.")
        #wordTrans.get_attribute("Helloo")
        time.sleep(2)

trnsword = Ceviri()
trnsword.transWord()
