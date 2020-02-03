from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usrnm = ""
pswrd = ""
class Yemek:
    def __init__(self, usrnm, pswrd):
        self.browser = webdriver.Chrome()
        self.usrnm = usrnm
        self.pswrd = pswrd

    def yemekLogin(self):
        self.browser.get("https://www.yemeksepeti.com/kktc")
        time.sleep(2)

        usrnmInput = self.browser.find_element_by_xpath("//*[@id='UserName']")
        pswrdInput = self.browser.find_element_by_xpath("//*[@id='password']")

        usrnmInput.send_keys(self.usrnm)
        pswrdInput.send_keys(self.pswrd)


        lgnBtn = self.browser.find_element_by_xpath("//*[@id='ys-fastlogin-button']")
        lgnBtn.click()
        time.sleep(3)

        ctySlct = self.browser.find_element_by_xpath("/html/body/header/div/div/div/div[2]/span/span[1]/span/span[2]")
        ctySlct.click()  #buraya kadar sıkıntı yok

        Slcttown = self.browser.find_element_by_xpath("//*[@id='ys-areaSelector-droparea']/span/span/span[1]/input")
        Slcttown.send_keys(Keys.ENTER)
        time.sleep(3)

        srchBtn = self.browser.find_element_by_xpath("/html/body/header/div/div/div/div[4]/input")
        srchBtn.click()
        srchBtn.send_keys("burger")
        srchBtn.send_keys(Keys.ENTER)
        time.sleep(2)

        frstFood = self.browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/a/i")
        frstFood.click()
        time.sleep(2)

        foodFrst = self.browser.find_element_by_xpath("//*[@id='cboxLoadedContent']/div/div[2]/div/div[2]/button")
        foodFrst.click()
        time.sleep(3)

        #sıfır hata..
        confrmOrder = self.browser.find_element_by_xpath("//*[@id='basket-container']/div[2]/div/div[5]/button")
        confrmOrder.click()
        time.sleep(3)

        payMent = self.browser.find_element_by_xpath("/html/body/div[1]/div/div/div[8]/div/div/div/div/div[2]/div/div[2]/label/input")
        payMent.click()

ymksprs = Yemek(usrnm,pswrd)
ymksprs.yemekLogin()
