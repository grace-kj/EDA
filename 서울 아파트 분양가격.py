#!/usr/bin/env python
# coding: utf-8

# In[6]:


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re

from plotnine import *



pre_sale= pd.read_csv('C:\\PycharmProjects\\bigdata\\Data\\분양가격\\전국_평균_분양가격_2018.7월_.csv', encoding='euc-kr', engine= 'python')
pre_sale.shape


# In[2]:


pre_sale.head()


# In[25]:


pre_sale.columns=['region', 'size', 'year', 'month', 'price']
pre_sale.info()


# In[24]:


import matplotlib as plt
import matplotlib.font_manager as fm


fm._rebuild()
plt.rc("font", family="NanumGothic")
fm.findfont("NanumGothic", rebuild_if_missing=False)


# In[26]:


#결측치 개수
pre_sale.isnull().sum()

#결측기 보기
import missingno as msno
msno.matrix(pre_sale, figsize=(18,6))


# In[28]:


#형변환
pre_sale['year']=pre_sale['year'].astype(str)
pre_sale['month']=pre_sale['month'].astype(str)

#to numeric에 넣기 위해
pre_sale_price= pre_sale['price']
pre_sale['price']= pd.to_numeric(pre_sale_price, errors='coerce')


# In[29]:


#분양가격 결측치 처리
pre_sale.isnull().sum()


# In[33]:


pre_sale.describe(include= [np.object])    #다른 변수도 같이


# In[34]:


#2017년 데이터만 보기
pre_sale_2017= pre_sale.loc[pre_sale['year']=='2017']
pre_sale_2017.shape


# In[35]:


pre_sale['size'].value_counts()


# In[37]:


#전국 평균 분양가격
# 숫자를 읽기 쉽게 하기 위해 지정
pd.options.display.float_format= '{:,.0f}'.format
#year를 기준으로 groupby 한 데이터 요약
pre_sale.groupby(pre_sale.year).describe().T 


# In[41]:


pre_sale.pivot_table('price', 'size', 'year')


# In[44]:


#size에서 전체로 되어있는 데이터만 가져와서 따로 테이블 만듬.
region_year_all= pre_sale.loc[pre_sale['size']=='전체']
region_year= region_year_all.pivot_table('price','region','year').reset_index()


# In[49]:





# In[51]:


region_year['price change']= (region_year['2018']- region_year['2015']).astype(int)
max_delta_price= np.max(region_year['price change'])*1000
min_delta_prive= np.min(region_year['price change'])*1000
mean_delta_price= np.mean(region_year['price change'])*1000

print("biggest price increase, {:,.0f}원 per m^2".format(max_delta_price))


# In[52]:


#지역별 분양가 합계
pre_sale.pivot_table('price','size','region')


# In[63]:


for i in range(len(pre_sale['size'])):
    if pre_sale['size'][i]=='전용면적 102㎡초과':
        pre_sale['size'][i]='102㎡ < space'
    elif pre_sale['size'][i]=='전용면적 60㎡이하':
        pre_sale['size'][i]='60㎡ <= space'
    elif pre_sale['size'][i]== '전용면적 60㎡초과 85㎡이하':
        pre_sale['size'][i]='60㎡ < space <= 85㎡'
    else:
        pre_sale['size'][i]= '85㎡ < space <= 102㎡'


# In[68]:


for i in range(len(pre_sale['region'])):
    if pre_sale['region'][i]=='강원':
        pre_sale['region'][i]='Gangwon'
    elif pre_sale['region'][i]=='경기':
        pre_sale['region'][i]='Gyounggi'
    elif pre_sale['region'][i]== '경남':
        pre_sale['region'][i]='Gyoungnam'
    elif pre_sale['region'][i]== '경북':
        pre_sale['region'][i]='Gyoungbook'
    elif pre_sale['region'][i]== '광주':
        pre_sale['region'][i]='Gwangju'
    elif pre_sale['region'][i]== '대구':
        pre_sale['region'][i]='Daegu'
    elif pre_sale['region'][i]== '대전':
        pre_sale['region'][i]='Daejwon'
    elif pre_sale['region'][i]== '부산':
        pre_sale['region'][i]='Busan'
    elif pre_sale['region'][i]== '서울':
        pre_sale['region'][i]='Seoul'
    elif pre_sale['region'][i]== '세종':
        pre_sale['region'][i]='Sejong'
    elif pre_sale['region'][i]== '울산':
        pre_sale['region'][i]='Ulsan'
    elif pre_sale['region'][i]== '인천':
        pre_sale['region'][i]='Incheon'
    elif pre_sale['region'][i]== '전남':
        pre_sale['region'][i]='Jeonnam'
    elif pre_sale['region'][i]== '전북':
        pre_sale['region'][i]='Jeonbook'
    elif pre_sale['region'][i]== '제주':
        pre_sale['region'][i]='Jeju'
    elif pre_sale['region'][i]== '충남':
        pre_sale['region'][i]='Chungnam'
    elif pre_sale['region'][i]== '충북':
        pre_sale['region'][i]= 'Chungbook'
   


# In[69]:


pre_sale.head()


# In[71]:



(ggplot(pre_sale, aes(x='region', y='price', fill='size'))
+ geom_bar(stat='identity', position='dodge')
+ ggtitle('new division appartment price')
+ theme(text= element_text(family='NanumGothic'),
       figure_size=(16,8))
)


# In[72]:


# 위에 그린 그래프를 지역별로 나눠 봅니다.
(ggplot(pre_sale)
 + aes(x='year', y='price', fill='size')
 + geom_bar(stat='identity', position='dodge')
 + facet_wrap('region')
 + theme(text=element_text(family='NanumGothic'),
         axis_text_x=element_text(rotation=70),
         figure_size=(12, 12))
)


# In[74]:


# 박스플롯을 그려봅니다.
(ggplot(pre_sale, aes(x='region', y='price', fill='size'))
 + geom_boxplot()
 + ggtitle('Domestic new appartment sales price by size')
 + theme(text=element_text(family='NanumGothic'),
         figure_size=(12, 6))
)


# In[75]:


pre_sale_seoul = pre_sale.loc[pre_sale['region']=='Seoul']
(ggplot(pre_sale_seoul)
 + aes(x='year', y='price', fill='size')
 + ggtitle('Seoul new appartment sales price by size and year')
 + geom_boxplot()
 + theme(text=element_text(family='NanumGothic'))
)


# In[76]:


# 2015년에서 2018년까지 분양가 차이가 가장 작았던 울산을 봅니다.
# 실제로는 분양가 차이가 적은 것이 아니라 결측치로 인해 분양가 차이가 적게 보였습니다.
(ggplot(pre_sale.loc[pre_sale['region']=='Ulsan'])
 + aes(x='region', y='price', fill='size')
 + geom_boxplot()
 + theme(text=element_text(family='NanumGothic'))
)


# In[ ]:




