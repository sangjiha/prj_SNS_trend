from selenium import webdriver
import sys
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.common.exceptions import InvalidSessionIdException

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

def cleansing(text):
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail주소제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]' # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text



driver = webdriver.Chrome('../chromedriver', options=options)


#로그인

LOGIN_URL = 'https://www.instagram.com/'

driver.get(LOGIN_URL)
time.sleep(2)
id = '01052942210'
password = 'Eun5375353!'
id_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input')[0]
id_input.send_keys(id)
password_input = driver.find_elements_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input')[0]
password_input.send_keys(password)
password_input.submit()

time.sleep(4)

driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')[0].click()
time.sleep(4)



LOGIN_INFO = {
    'id': '01052942210',
    'pass': 'Eun5375353!'
}
s = requests.Session()

with requests.Session() as s:
    res = s.post(LOGIN_URL, data=LOGIN_INFO, verify=False, allow_redirects=False)
    print(res.headers.keys)
    # 쿠키와 헤더에 포함된 302 Location 값을 가져온다.
    # 이때, 헤더에 설정된 쿠키와 함께 Location으로 Get Request 를 보내면 된다.
    redirect_cookie = res.headers['Set-Cookie']
    print(redirect_cookie)
    #redirect_url = res.headers['Location']
    #print(redirect_url)
    headers = {"Cookie": redirect_cookie}

    # Location 주소로 Get Request 호출
    s.get(LOGIN_URL, headers=headers)


time.sleep(1)



#키워드 크롤링 시작

keyword = "치즈볼"

url = "https://www.instagram.com/explore/tags/{}/".format(keyword)
instagram_title = []
instagram_dates = []
driver.get(url)
time.sleep(3)
count = driver.find_element_by_css_selector('#react-root > section > main > header > div.WSpok > div > div.Igw0E.IwRSH.eGOV_._4EzTm.a39_R > span > span').text
count = count.replace(',','')
count = int(count)
print(count)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
for i in range(1,count):
    time.sleep(2)
    try:
        #글내용 가져오기
        title = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span').text
        title = cleansing(title)
        title = title.replace('\n', ' ')


        #날짜 가져오기
        date = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time') #날짜가 들어있는 xpath
        date = date[0].get_attribute('title')  #날짜만 가져오기

        instagram_title.append(title)
        instagram_dates.append(date)


    except:
        print(i, 'title/dates error')
        #도중에 에러가 발생했을 경우, 내용과 날짜에 NaN값을 추가

        instagram_title.append("NaN")
        instagram_dates.append('NaN')


    try:
        #다음페이지로 넘어가는 '>'표시 클릭
        driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow').click()

    except:
        print(i, 'next page error')
        #driver.close() # date = datum2.text #print(date)

    if i % 100 == 0:
        df_instagram = pd.DataFrame({'date': instagram_dates, 'title': instagram_title})
        df_instagram.to_csv('prj_sns_trend_crawling_instagram_{}.csv'.format(i))
        print(i)
    time.sleep(1)

df_instagram= pd.DataFrame({'date': instagram_dates, 'title' : instagram_title})



