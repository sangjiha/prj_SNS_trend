
from selenium import webdriver
import sys

from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#notification 없애기
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome('../chromedriver', options=options)



driver.get('https://www.instagram.com/')

time.sleep(3) #웹 페이지 로드를 보장하기 위해 3초 쉬기

#

id = '01052942210'
password = 'Eun5375353!'
id_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')[0]
id_input.send_keys(id)
password_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')[0]
password_input.send_keys(password)
password_input.submit()

time.sleep(4)

#driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(3)').click()
#time.sleep(3)
driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')[0].click()
time.sleep(4)
#driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0].click() 위에 import로 해결


