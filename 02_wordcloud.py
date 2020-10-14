#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from konlpy.tag import Okt 


# In[2]:


df = pd.read_csv('./facebook1.csv', index_col=0)
print(df.info()) 
df.drop_duplicates(inplace=True)
df.dropna(subset=['title'],how='any',inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.info()) 


# In[3]:


#stopwords 현 디렉토리에 추가 해야함 
stopwords = pd.read_csv('./stopwords.csv',index_col=0) 
stopwords.head()


# In[4]:


#데이터 전처리
okt = Okt()


# In[5]:


#stores = pd.read_csv('./stores.csv', 
#                    encoding='euc-kr', index_col=0)
#stores = stores.reset_index()
stores = pd.read_excel('./프렌차이즈.xlsx')
stores
stores.reset_index(drop=True, inplace=True)
print(stores.info()) 
stores.columns





# In[6]:



#stores_name = stores.iloc[:,1]


#stores_name


# In[7]:


"""
cleaned_sentences = []

for sentence in df['title']:
    sentence = re.sub('[^a-zA-Z가-힣]',' ',sentence)
    #token = okt.pos(sentence, norm=True, stem=True)
    token = sentence.split(' ')
    cleaned_df_token = pd.DataFrame(token, columns=['word'])
    #cleaned_df_token = df_token[(df_token['class']=='Noun')|(df_token['class']=='Verb')|(df_token['class']=='Adjective')]
    #cleaned_df_token = df_token[(df_token['class']=='Noun')]
    words = []
    for word in cleaned_df_token['word']:
       if len(word)>1: 
          if word not in (list(stopwords['stopword'])): 
              words.append(word)
          else: print(word) 
       else: print(word)    
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_content'] = cleaned_sentences
"""


# In[15]:


cleaned_sentences = []

for sentence in df['title']:
    E_sentence = re.sub('[^a-zA-Z]',' ', sentence)
    #token = okt.pos(sentence, norm=True, stem=True)
    E_token = E_sentence.split(' ')
    #cleaned_df_token = pd.DataFrame(E_token, columns=['word'])
    K_sentence = re.sub('[^가-힣]',' ', sentence)
    K_token = okt.pos(K_sentence, norm=True, stem=True)
    K_token = pd.DataFrame(K_token, columns=['word','class'])
    #cleaned_df_token = df_token[(df_token['class']=='Noun')|(df_token['class']=='Verb')|(df_token['class']=='Adjective')]
    cleaned_K_token = K_token[(K_token['class']=='Noun')]
    #데이터프레임 word 컬럼 끼리 합치기 
    token = E_token + list(cleaned_K_token['word'])
    cleaned_token = pd.DataFrame(token, columns=['word'])
    words = []
    for word in cleaned_token['word']:
       if len(word)>1: 
          if word not in (list(stopwords['stopword'])): 
              words.append(word)
          else: print(word) 
       else: print(word)    
    cleaned_sentence = ' '.join(words)
    cleaned_sentences.append(cleaned_sentence)

df['cleaned_content'] = cleaned_sentences


# In[17]:


print(df.info())
print(df.head(10))


# In[19]:


store_cleaned_content = []
for sentence in df['cleaned_content']:
    token = sentence.split(' ')
    tokens = pd.DataFrame(token, columns=['token'])
    for word in tokens['token']:
       if word not in (list(stores['치킨'])): 
          print("nostore")
       else: 
          store_cleaned_content.append(sentence)
          print(word)
df['store_cleaned_content'] = store_cleaned_content3
        


# In[20]:


store_cleaned_content = []
for sentence in df['cleaned_content']:
    word = sentence.split(' ')
    if word not in (list(stores['치킨'])): 
            print("nostore")
    else: 
             
            store_cleaned_content.append(sentence)
            print(word)
df['store_cleaned_content'] = store_cleaned_content


# In[8]:


print(df.head())
print(df.info())


# In[18]:


#필요없는 title 컬럼의 데이터들을 '맛집'으로 통일해서 채움 -> 동일한 컬럼끼리 one sentence로 합치기 위함 

df['title']='맛집'


# In[19]:


print(df.head())


# In[20]:


#one sentence 
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


# In[29]:


#one sentence로 합쳐진 데이터를 X에 저장 
X=df_review_one_sentence
print(X.head())


# In[30]:


import pandas as pd
pd.set_option('display.max_row',500)
pd.set_option('display.max_columns',100)
pd.set_option('display.unicode.east_asian_width',True) 
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud,STOPWORDS
from PIL import Image 
import collections


# In[31]:


fontpath = './malgun.ttf'


# In[32]:


#바꾸지 X
book_title='맛집'


# In[33]:


book_idx = X[X['title']==book_title].index[0]


# In[34]:


tokened_content_words = X['review_one_sentence'][book_idx].split(' ')


# In[35]:


textdict = collections.Counter(tokened_content_words)


# In[39]:


wordcloude_img = WordCloud(background_color = 'white', max_words=10, font_path=fontpath).generate_from_frequencies(textdict)
plt.figure(figsize=(8,8))
plt.imshow(wordcloude_img, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[ ]:




