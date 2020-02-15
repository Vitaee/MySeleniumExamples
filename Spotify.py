from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = ""
password = ""

class Spotify:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.browser = webdriver.Chrome()

	def playMusic(self):
		self.browser.get("https://www.spotify.com/tr/")
		self.browser.maximize_window()
		try:
			firstClick = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/header/div/nav/ul/li[6]/a")));
			firstClick.click()

		except:
			print("Oturum aç tıklanılamadı!")

		try:
			secondClick = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/body/div[1]/div[2]/div/div[2]/div/a")));
			secondClick.click()

		except:
			print("Facebook ile oturum açılamadı!")

		try:
			fcbkName = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, "email")))
			fcbkPass = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.ID, "pass")))
			fcbkName.send_keys(self.username)
			fcbkPass.send_keys(self.password)
		except:
			print("Kullanıcı bilgileri girilemedi!")

		try:
			lgnButton = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.ID, "loginbutton")));
			lgnButton.click()

		except:
			print("Login butonuna tıklanılamadı!")

		try:
			webMusic = WebDriverWait(self.browser,15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/footer/nav/div[2]/dl[3]/dd[2]/a")));
			webMusic.click()

		except:
			print("Web çalar tıklanılamadı!")

		try:
			musicPlay = WebDriverWait(self.browser,15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[4]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button")));
			musicPlay.click()

		except:
			print("Hata!")

		#dilersek bir kere daha tıklanılmasını sağlayabiliriz..

		#try:
		#	musicPlay.click()

		#except:
		#	print("Müzik başlatılamadı !")


sptfy = Spotify(username,password)
sptfy.playMusic()