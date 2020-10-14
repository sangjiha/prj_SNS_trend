#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


# In[3]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)

body = driver.find_element_by_tag_name('body')

title_name = []
url = 'https://www.youtube.com/results?search_query=%EC%B9%98%EC%A6%88%EB%B3%BC&sp=EgIIBA%253D%253D' #유튜브 키워드 검색 URL
driver.get(url)
time.sleep(0.4)
#driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/div/ytd-toggle-button-renderer/a/paper-button/yt-formatted-string').click() #필터 클릭
#time.sleep(0.4)
#driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[1]/div[2]/ytd-search-sub-menu-renderer/div[1]/iron-collapse/div/ytd-search-filter-group-renderer[1]/ytd-search-filter-renderer[5]/a/div/yt-formatted-string').click() #올해 클릭
#time.sleep(0.5)

for i in range(1,500):
    for j in range(1,20):
        try:
            title = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[{0}]/div[3]/ytd-video-renderer[{1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'.format(i,j)).text
            title_name.append(title)
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        except:
            continue

df = pd.DataFrame({'title':title_name}) #키워드 먹방 검색 시, 제목 크롤링
print(df.info())
df


# In[ ]:


df.to_csv('./datasets/sns_trend_youtube_crawling3_맛집.csv')


# In[2]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)

body = driver.find_element_by_tag_name('body')

title_name = []
date = []
url = 'https://www.youtube.com/results?search_query=%EC%B9%98%EC%A6%88%EB%B3%BC&sp=EgQIBRAB' #치즈볼 올해 검색
driver.get(url)
time.sleep(0.4)
for i in range(1,50): #500까지
    for j in range(1,20): #20까지 
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[{0}]/div[3]/ytd-video-renderer[{1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'.format(i,j)).click()
            time.sleep(5.0)
            title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
            dates = driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text #날짜
            time.sleep(5.0)
            print(title)
            print(date)
            title_name.append(title)
            date.append(dates)
            driver.back()
            time.sleep(5.0)
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.PAGE_DOWN)
        except:
            continue

df = pd.DataFrame({'title':title_name, 'date':date}) #키워드 먹방 검색 시, 제목 크롤링
print(df.info())
df


# In[5]:


df.to_csv('./datasets/sns_trend_youtube_crawling1013.csv')


# In[7]:


print(df.tail())


# In[ ]:





# In[4]:


df['date'] = pd.to_datetime(df['date']) #Date 열에 덮어 씌워짐 
df.set_index('date', inplace=True) #Date 열을 인덱스로 설정
print(raw_data.head())


# In[6]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)

body = driver.find_element_by_tag_name('body')

title_name = []
date = []
url = 'https://www.youtube.com/results?search_query=%EC%B9%98%EC%A6%88%EB%B3%BC&sp=EgQIBRAB' #치즈볼 올해 검색
driver.get(url)
time.sleep(0.4)
for i in range(1,50): #500까지
    for j in range(1,20): #20까지 
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[{0}]/div[3]/ytd-video-renderer[{1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'.format(i,j)).click()
            time.sleep(5.0)
            title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
            dates = driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text #날짜
            time.sleep(5.0)
            print(title)
            print(date)
            title_name.append(title)
            date.append(dates)
            driver.back()
            time.sleep(5.0)
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.PAGE_DOWN)
        except:
            continue

df = pd.DataFrame({'title':title_name, 'date':date}) #키워드 먹방 검색 시, 제목 크롤링
print(df.info())
df


# In[9]:



    
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver', options=options)

body = driver.find_element_by_tag_name('body')

title_name = []
date = []
url = 'https://www.youtube.com/results?search_query=%EC%B9%98%EC%A6%88%EB%B3%BC&sp=EgIIAw%253D%253D' #치즈볼 이번주 
driver.get(url)
time.sleep(0.4)
for i in range(1,50): #500까지
    for j in range(1,20): #20까지 
        try:
            driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[{0}]/div[3]/ytd-video-renderer[{1}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'.format(i,j)).click()
            time.sleep(5.0)
            title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
            dates = driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text #날짜
            time.sleep(5.0)
            print(title)
            print(date)
            title_name.append(title)
            date.append(dates)
            driver.back()
            time.sleep(5.0)
            body = driver.find_element_by_tag_name('body')
            body.send_keys(Keys.PAGE_DOWN)
        except:
            continue

df_thisweek = pd.DataFrame({'title':title_name, 'date':date}) #키워드 먹방 검색 시, 제목 크롤링
print(df_thisweek.info())
df_thisweek


# In[ ]:




