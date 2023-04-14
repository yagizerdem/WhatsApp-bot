from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time


#object of ChromeOptions class
o = webdriver.ChromeOptions()
#adding specific Chrome Profile Path
o.add_argument("user-data-dir=C:\\Users\\yagiz\\AppData\\Local\\Google\\Chrome\\User Data")
o.add_argument("profile-directory=Profile 1")
#set chromedriver.exe path
driver = webdriver.Chrome(executable_path="C:/Users/yagiz/Desktop/Python/python selenium projects/chromedriver.exe", options=o)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://web.whatsapp.com/")

target_boy_xpath = "/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div/div/div[10]/div/div/div/div[2]/div[2]/div[1]/span/span"
message = "This is a bot written by python selenium"

WebDriverWait(driver, timeout=60).until(
    ec.visibility_of_element_located((By.XPATH, target_boy_xpath ))
)

driver.find_element(By.XPATH, target_boy_xpath).click()

text_area = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]")

for i in range(4):
    text_area.send_keys(message)
    text_area.send_keys(Keys.ENTER)
    time.sleep(0.5)

time.sleep(4)
driver.close()

