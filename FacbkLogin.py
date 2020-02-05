from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys


mailname = ""
password1 = ""

class Facebook:
    def __init__(self,mailname,password1):
        self.browser = webdriver.Chrome()
        self.mail = mailname
        self.password1 = password1

    def singIn(self):
        self.browser.get("https://www.facebook.com/login/")
        
        mailnameInput = self.browser.find_element_by_xpath("//*[@id='email']")
        password1Input = self.browser.find_element_by_xpath("//*[@id='pass']")

        mailnameInput.send_keys(self.mail)
        password1Input.send_keys(self.password1)
        password1Input.send_keys(Keys.ENTER)
        
 facbk = Facebook(mailname,password1)
 facbk.singIn()
