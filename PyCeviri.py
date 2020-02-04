from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time

class Ceviri:
    def __init__ (self):
        self.browser = webdriver.Chrome()
    def transWord(self):
        self.browser.get("https://www.google.com.tr")
        time.sleep(2)
        wordTrans = self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        wordTrans.send_keys("google translate")
        srchBtn = self.browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
        srchBtn.click()

        
        a = input("Lütfen yabancı kelimenizi giriniz:\n ")
        time.sleep(2)
        wrdTrns = self.browser.find_element_by_xpath("//*[@id='tw-source-text-ta']")
        wrdTrns.send_keys(a)

        Trnsword = self.browser.find_element_by_xpath("//*[@id='tw-tl']")
        Trnsword.click()

        detectLng = self.browser.find_element_by_xpath("//*[@id='tl_list-search-box']")
        detectLng.send_keys("Turkish")
        #Lngdetect = self.browser.find_element_by_xpath("//*[@id='tw-container']/g-expandable-container/div/div/div[6]/g-expandable-container/div/g-expandable-content/span/div/div[2]/div[2]/div[96]")
        detectLng.send_keys(Keys.ENTER)


trnsword = Ceviri()
trnsword.transWord()
