from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YolTarif:
    def __init__(self):
        self.tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.tarayici.maximize_window()
        self.tarayici.get('https://www.google.nl/maps/')

    def Islem(self):

        self.yol_butonu = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.ID, 'searchbox-directions')))
        self.yol_butonu.click()

        self.baslangic = input("Please enter start point (City/Country)")
        self.baslangic_yeri = WebDriverWait(self.tarayici, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="sb_ifc51"]/input')))
        self.baslangic_yeri.send_keys(self.baslangic)

        self.son_durak = input("Please enter end point (City/Country)")
        self.end_point = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sb_ifc52"]/input')))
        self.end_point.click()
        self.end_point.send_keys(self.son_durak)
        self.end_point.send_keys(Keys.ENTER)

        sleep(2)

        source = self.tarayici.page_source
        soup = BeautifulSoup(source, 'html.parser')
        try:
            data = soup.find('h1', id='section-directions-trip-title-0')
            yol = data.text
            print("Araba ile " + yol)
        except:
            data2 = soup.find('h1', id='section-directions-trip-title-0')
            for item in data2:
                items= item.find('span',jstcache='1020')
                print("Araba ile " + items.text)

        data1 = soup.find_all('div', class_='section-directions-trip-numbers')
        for item in data1:
            items = item.find('span')
            sure = items.text
            print("Araba ile " + sure)
            break

yolTarif= YolTarif()
yolTarif.Islem()
