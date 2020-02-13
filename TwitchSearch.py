from selenium import webdriver
#https://selenium-python.readthedocs.io/
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Twitch: 
	def __init__(self):
		self.browser = webdriver.Chrome()

	def openTwitch(self):
		self.browser.get("https://www.twitch.tv/")
		self.browser.maximize_window()

		try:
			barClick = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/nav/div/div[2]/div/div')));
			barClick.click()
		except:
			print("Element not clickable")

	

		try:
			searchBar = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH,'(//input[@type="search"])[1]')))
			searchBar.send_keys("Jahrein")
			searchBar.send_keys(Keys.ENTER)
		except:
			print("Element not writable")

		try:
			firstMan = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/div/main/div/div[3]/div/div/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/strong/a")));
			firstMan.click()
		except:
			print("Can't clikc first streamer")

twtch = Twitch()
twtch.openTwitch()

