
from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys
from time import time

gitname = "Account Name"
gitpass = "password"
class Github:
    def __init__(self,gitname,gitpass):
        self.browser = webdriver.Chrome()
        self.gitname = gitname
        self.gitpass = gitpass

    def singn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        gitnameInput = self.browser.find_element_by_xpath("//*[@id='login_field']")
        gitpassInput = self.browser.find_element_by_xpath("//*[@id='password']")

        gitnameInput.send_keys(self.gitname)
        gitpassInput.send_keys(self.gitpass)
        gitpassInput.send_keys(Keys.ENTER)
        time.sleep(2)

githb = Github(gitname, gitpass)
githb.singn()
