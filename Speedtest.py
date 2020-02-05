from selenium import webdriver


class Speed:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def pressButon(self):
        self.browser.get("https://www.speedtest.net/")
       
        butonPress = self.browser.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[2]/div[3]/div[1]/a")
        butonPress.click()
      

sped = Speed()
sped.pressButon()
