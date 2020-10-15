#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt 
from ckonlpy.tag import Twitter #prompt에서 pip install customized_konlpy 로 패키지 설치


# In[2]:


#크롤링한 데이터 파일 불러오기
#중복제거 및 널값제거 
df = pd.read_csv('./crawling_from20200101_to20201015.csv', index_col=0)
df.drop_duplicates(inplace=True)
df.dropna(subset=['title'],how='any',inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.info()) 


# In[3]:


#한국어에 사용할 토크나이저
twitter = Twitter()


# In[4]:


#토큰화에 제외할 단어 토크나이저 딕셔너리에 추가 
twitter.add_dictionary(['뿌링클','맛스타그램', '맛스타', '푸라닭', '스타그램', '인스타', '또래오래', '배달의민족','배민', 'instagram', '뿌링클', '고추바사삭', '뿌링뿌링','뿌링뿌링소스' ,'뿌링소스', '또래오래', '인스타 그램','인스타그램', '황금올리브','네고왕','맘스터치','에어프라이어','블랙치즈볼','블랙알리오','청년치킨','청년피자'], 'Noun',force=True)

#for word in imp_wrd['important_words']:
#    twitter.add_dictionary('{}', 'Noun').format(word)
    



# In[5]:


#딕셔너리 추가된 것 테스트 
twitter.morphs('일주일만에 다시 찾은 뿌링클 맛스타그램 네고왕')


# In[6]:


#stopwords 현 디렉토리에 추가 해야함 
stopwords = pd.read_csv('./stopwords.csv',  encoding='CP949' ,index_col = 0) 
print(stopwords.head())
print(stopwords.tail())


# In[7]:


#프랜차이즈 리스트 
stores = pd.read_excel('./프렌차이즈.xlsx')
stores
stores.reset_index(drop=True, inplace=True)
print(stores.info()) 
stores.columns
#stores = pd.read_csv('./stores.csv', 
#                    encoding='euc-kr', index_col=0)


# In[13]:


#토큰화 및 텍스트 데이터 전처리 
cleaned_sentences = []

for sentence in df['title']:
    E_sentence = re.sub('[^a-zA-Z]',' ', sentence)  #영어텍스트만 뽑아오기 
    E_token = E_sentence.split(' ')   #영어텍스트를 띄어쓰기 기준으로 토큰화 
    K_sentence = re.sub('[^가-힣]',' ', sentence)  #한글텍스트만 뽑아오기
    K_token = twitter.nouns(K_sentence) #한글텍스트를 토큰화 및 명사만 남기기 
    K_token = pd.DataFrame(K_token, columns=['word'])   #토큰화된 한글텍스트를 다시 데이터프레임으로 만들기
    token = E_token + list(K_token['word'])    #토큰화된 한글, 영어텍스트를 합치기 
    cleaned_token = pd.DataFrame(token, columns=['word'])   #합친 것을 다시 데이터프레임으로 만들기 
    words = []
    for word in cleaned_token['word']:  #불용어 제거 
       if len(word)>1: 
          if word not in (list(stopwords['stopword'])): 
              words.append(word)
          else: print(word) 
       else: print(word)    
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_content'] = cleaned_sentences


# In[ ]:


"""
#형용사와 명사만 남길경우 사용 
cleaned_sentences = []

for sentence in df['title']:
    E_sentence = re.sub('[^a-zA-Z]',' ', sentence)  #영어텍스트를 띄어쓰기 기준으로 토큰화 
    E_token = E_sentence.split(' ')
    K_sentence = re.sub('[^가-힣]',' ', sentence)  #한글텍스트를 토큰화 
    K_token = twitter.pos(K_sentence)
    K_token = pd.DataFrame(K_token, columns=['word','class'])   #토큰화된 한글텍스트를 다시 데이터프레임으로 만들기
    K_token = K_token[(K_token['class']=='Noun')|(K_token['class']=='Adjective')] 
    token = E_token + list(K_token['word'])    #토큰화된 한글, 영어텍스트를 합치기 
    cleaned_token = pd.DataFrame(token, columns=['word'])   #합친 것을 다시 데이터프레임으로 만들기 
    words = []
    for word in cleaned_token['word']:  #불용어 제거 
       if len(word)>1: 
          if word not in (list(stopwords['stopword'])): 
              words.append(word)
          else: print(word) 
       else: print(word)    
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_content'] = cleaned_sentences
"""


# In[14]:


print(df.info())
print(df.head(30))


# In[15]:


#프랜차이즈 리스트의 치킨 프랜차이즈들이 언급된 문장만 남기기 
store_cleaned_content = []
for sentence in df['cleaned_content']:
    token = sentence.split(' ')
    tokens = pd.DataFrame(token, columns=['token'])
    for word in (list(tokens['token'])):

            if word in (list(stores['치킨'])): 
                store_cleaned_content.append(sentence)
                break
            

    
new_df = pd.DataFrame({'store_cleaned_content': store_cleaned_content})

print(new_df.info())        


# In[16]:


print(new_df.head())
print(new_df.info())


# In[17]:


#필요없는 title 컬럼의 데이터들을 '치즈볼'로 통일해서 채움 -> 동일한 컬럼을 기준으로 one sentence로 합치기 위함 

df['title']='치즈볼'


# In[18]:


print(df.head())


# In[19]:


#one sentence 만들기
review_one_sentences = []
titles = []

for title in df['title'].unique():
    temp = df[df['title']==title]['cleaned_content']
    review_one_sentence = ' '.join(list(temp)) 
    review_one_sentences.append(review_one_sentence)
    titles.append(title)
    
df_review_one_sentence = pd.DataFrame({'title':titles, 'review_one_sentence':review_one_sentences})
print(df_review_one_sentence.head())
print(df_review_one_sentence.info())


# In[20]:


#one sentence로 합쳐진 데이터를 X에 저장 
X=df_review_one_sentence
print(X.head())


# In[21]:


#워드클라우드 합치기 
import pandas as pd
pd.set_option('display.max_row',500)
pd.set_option('display.max_columns',100)
pd.set_option('display.unicode.east_asian_width',True) 
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud,STOPWORDS
from PIL import Image 
import collections


# In[22]:


fontpath = './malgun.ttf'


# In[23]:


#바꾸지 X 
_title='치즈볼'


# In[24]:


_idx = X[X['title']==_title].index[0] 


# In[25]:


tokened_content_words = X['review_one_sentence'][_idx].split(' ')


# In[26]:


textdict = collections.Counter(tokened_content_words)


# In[27]:


wordcloude_img = WordCloud(background_color = 'white', max_words=300, font_path=fontpath).generate_from_frequencies(textdict)
plt.figure(figsize=(16,16))
plt.imshow(wordcloude_img, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[ ]:




