from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usernm = "canilguu@gmail.com"
password2 = "cansoft88"

class Twitter:
    def __init__(self, usernm, password2):
        self.browser = webdriver.Chrome()
        self.usernm = usernm
        self.password2 = password2

    def twittSing(self):
        self.browser.get("https://twitter.com/login?lang=tr")  #google chromedaki ile aynı olmalı!
        self.browser.maximize_window()
            
        try:
            usernameInput = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH , "//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[1]/label/div[2]/div/input")));
            passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[2]/label/div[2]/div/input")

            usernameInput.send_keys(self.usernm)
            passwordInput.send_keys(self.password2)
        except:
            print("Mail/Şifre girilemedi!")

        try:
            btnSubmit = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[1]/main/div/div/form/div/div[3]/div/div")));
            btnSubmit.click()

        except:
            print("Giriş butonuna tıklanılmadı!")

        try:
            searhBtn = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")));
            searhBtn.send_keys("python")
            searhBtn.send_keys(Keys.ENTER)  
                
        except:
            print("Arama çubuğu kullanılamadı!")

        try:
            likeBut = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div/div[8]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[2]")));
            likeBut.click()
        except:
            print("Gönderi beğenilemedi!")

            
twitterr = Twitter(usernm,password2)
twitterr.twittSing()