#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df= pd.read_csv("C:\\PycharmProjects\\bigdata\\Data\\시군구별_이동자수_2021.csv", encoding='euc-kr')
df.columns=df.loc[1]

df.head()



# In[2]:


dataset = df[['행정구역(시군구)별','총전입 (명)',
              '총전출 (명)']]
dataset.columns=['행정구역(시군구)별','총전입(11월)', '총전입(12월)','총전입(1월)','총전출(11월)','총전출(12월)','총전출(1월)']
dataset.head()


# In[3]:


dataset= dataset.loc[4:28]
dataset


# In[4]:


type(dataset.iloc[[1],[1]])


# In[5]:


dataset.iloc[:,[1,2,3,4,5,6]]=dataset.iloc[:,[1,2,3,4,5,6]].astype(int)


# In[6]:


#총전입 총전출 차이 계산
dataset['차이']=(dataset['총전입(11월)']+ dataset['총전입(12월)']+dataset['총전입(1월)'])-(dataset['총전출(11월)']+dataset['총전출(12월)']+dataset['총전출(1월)'])
dataset


# In[10]:


dataset.columns=['region', 'wholeCome(11)', 'wholeCome(12)', 'wholeCome(1)',' wholeGo(11)','wholeGo(12)', 'wholeGo(1)','difference']
dataset


# In[34]:


dataset['region'].iloc[0]


# In[36]:


for i in range(len(dataset['region'])):
    if dataset['region'].iloc[i]=='종로구':
        dataset['region'].iloc[i]='Jongno'
    elif dataset['region'].iloc[i]=='중구':
        dataset['region'].iloc[i]='Junggu'
    elif dataset['region'].iloc[i]== '용산구':
        dataset['region'].iloc[i]='Yongsan'
    elif dataset['region'].iloc[i]== '성동구':
        dataset['region'].iloc[i]='Seoungdong'
    elif dataset['region'].iloc[i]== '광진구':
        dataset['region'].iloc[i]='Gwangjin'
    elif dataset['region'].iloc[i]== '동대문구':
        dataset['region'].iloc[i]='Dongdaemun'
    elif dataset['region'].iloc[i]== '중랑구':
        dataset['region'].iloc[i]='Jungnang'
    elif dataset['region'].iloc[i]== '성북구':
        dataset['region'].iloc[i]='Seoungbuk'
    elif dataset['region'].iloc[i]== '강북구':
        dataset['region'].iloc[i]='Gangbuk'
    elif dataset['region'].iloc[i]== '도봉구':
        dataset['region'].iloc[i]='Dobong'
    elif dataset['region'].iloc[i]== '노원구':
        dataset['region'].iloc[i]='Nowon'
    elif dataset['region'].iloc[i]== '은평구':
        dataset['region'].iloc[i]='Eunpyeoung'
    elif dataset['region'].iloc[i]== '서대문구':
        dataset['region'].iloc[i]='Seodaemun'
    elif dataset['region'].iloc[i]== '마포구':
        dataset['region'].iloc[i]='Mapo'
    elif dataset['region'].iloc[i]== '양천구':
        dataset['region'].iloc[i]='Yangcheon'
    elif dataset['region'].iloc[i]== '강서구':
        dataset['region'].iloc[i]='Gangseo'
    elif dataset['region'].iloc[i]== '구로구':
        dataset['region'].iloc[i]= 'Guro'
    elif dataset['region'].iloc[i]== '금천구':
        dataset['region'].iloc[i]= 'Geumcheon'
    elif dataset['region'].iloc[i]== '영등포구':
        dataset['region'].iloc[i]= 'Yeongdeungpo'
    elif dataset['region'].iloc[i]== '동작구':
        dataset['region'].iloc[i]= 'Dongjak'
    elif dataset['region'].iloc[i]== '관악구':
        dataset['region'].iloc[i]= 'Gwanak'
    elif dataset['region'].iloc[i]== '서초구':
        dataset['region'].iloc[i]= 'Seocho'
    elif dataset['region'].iloc[i]== '강남구':
        dataset['region'].iloc[i]= 'Gangnam'
    elif dataset['region'].iloc[i]== '송파구':
        dataset['region'].iloc[i]= 'Songpa'
    elif dataset['region'].iloc[i]== '강동구':
        dataset['region'].iloc[i]= 'Gangdong'


# In[50]:


dataset


# In[51]:


dataset['difference'].sort_values().plot(kind='barh', grid= True, figsize=(10,10))


# In[ ]:





# In[ ]:




