#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import os
import pandas as pd

#다운받은 csv 불러오기

df= pd.read_csv("C:\\PycharmProjects\\bigdata\\Data\\소상공인상가상권정보_서울_202012.csv",engine='python', sep=',')

print(df.columns)


# In[2]:


print('상권업종대분류명', set(df['상권업종대분류명']))
print('상권업종중분류명', set(df['상권업종중분류명']))


# In[3]:


dataset = df[['상호명','지점명',
              '상권업종대분류명', '상권업종중분류명',
              '시도명', '시군구명', '행정동명',
              '위도', '경도']]
dataset.head()


# In[4]:


df_coffee = dataset[(dataset['상권업종중분류명']=='커피점/카페')]
df_coffee.index = range(len(df_coffee))
print('서울시 내 커피 전문점 점포 수 :', len(df_coffee))
df_coffee.head()


# In[5]:


df_seoul_starbucks = df_coffee[df_coffee['상호명'].str.contains('스타벅스')]
df_seoul_starbucks.index = range(len(df_seoul_starbucks))
print('서울시 내 스타벅스 점포 수 :', len(df_seoul_starbucks))
df_seoul_starbucks.head()


# In[6]:


df_seoul_ediya = df_coffee[df_coffee['상호명'].str.contains('이디야')]
df_seoul_ediya.index = range(len(df_seoul_ediya))
print('서울시 내 이디야 점포 수 :', len(df_seoul_ediya))
df_seoul_ediya.head()


# In[7]:


starbucks_gu = df_seoul_starbucks.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
starbucks_gu = starbucks_gu.reset_index()
starbucks_gu = starbucks_gu.set_index('시군구명')

starbucks_gu


# In[8]:


ediya_gu = df_seoul_ediya.groupby('시군구명')['상호명'].count().to_frame().sort_values(by='상호명', ascending=False)
ediya_gu = ediya_gu.reset_index()
ediya_gu = ediya_gu.set_index('시군구명')
ediya_gu


# In[9]:


import json

geo_path = 'C:\\PycharmProjects\\bigdata\\Data\\geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))


# In[12]:


import folium

loc = [37.5502, 126.982] # 위도(N), 경도(E)
data_size = len(df_seoul_starbucks)

# 지도 정의
map_starbucks = folium.Map(location=loc, zoom_start=12)
map_starbucks.choropleth(geo_data=geo_str,
              data = starbucks_gu['상호명'],
              columns=[starbucks_gu.index, starbucks_gu['상호명']],
              fill_color='PuRd',
              key_on='feature.id')


# 포인트 마커 추가

for i in range(data_size):

    folium.Marker(list(df_seoul_starbucks.iloc[i][['위도', '경도']]),
                 popup=df_seoul_starbucks.iloc[i][['지점명']],
                 icon=folium.Icon(color='green')).add_to(map_starbucks)

map_starbucks


# In[14]:


# 위치 파라미터 설정
loc = [37.5502, 126.982] # 위도(N), 경도(E)
data2_size = len(df_seoul_ediya)

# 지도 정의
map_ediya = folium.Map(location=loc, zoom_start=12)
map_ediya.choropleth(geo_data=geo_str,
              data = ediya_gu['상호명'],
              columns=[ediya_gu.index, ediya_gu['상호명']],
              fill_color='PuRd',
              key_on='feature.id')


# 포인트 마커 추가

for i in range(data2_size):

    folium.Marker(list(df_seoul_ediya.iloc[i][['위도', '경도']]),
                 popup=df_seoul_ediya.iloc[i][['지점명']],
                 icon=folium.Icon(color='blue')).add_to(map_ediya)

map_ediya


# In[29]:


# 위치 파라미터 설정
loc = [37.5502, 126.982] # 위도(N), 경도(E)

data_size = len(df_seoul_starbucks)
data2_size = len(df_seoul_ediya)

# 지도 정의
map = folium.Map(location=loc,
                 tiles = 'Stamen Toner',
                 zoom_start=11)

# 포인트 마커 추가

for i in range(data_size):

    folium.CircleMarker(list(df_seoul_starbucks.iloc[i][['위도', '경도']]),
                 radius=5, weight= 1,
                 color='green').add_to(map)


for i in range(data2_size):

    folium.CircleMarker(list(df_seoul_ediya.iloc[i][['위도', '경도']]),
                 radius=5, weight=1,
                 color='blue').add_to(map)


map


# In[16]:


# 위치 파라미터 설정

# 강남역 좌표
loc = [37.497895, 127.027565] # 위도(N), 경도(E)

data_size = len(df_seoul_starbucks)
data2_size = len(df_seoul_ediya)

# 지도 정의
map = folium.Map(location=loc,
                 tiles = 'Stamen Toner', # 'OpenStreetMap'
                 zoom_start=14)

# 포인트 서클 추가

for i in range(data_size):

    folium.Circle(list(df_seoul_starbucks.iloc[i][['위도', '경도']]),
                  radius = 100,
                  popup = df_seoul_starbucks.iloc[i]['지점명'],
                  color = '#2c9147',fill_color = '#2c9147').add_to(map)

for i in range(data2_size):

    folium.Circle(list(df_seoul_ediya.iloc[i][['위도', '경도']]),
                  radius = 100,
                  popup = df_seoul_ediya.iloc[i]['지점명'],
                  color = '#32408c',fill_color = '#32408c').add_to(map)

map


# In[ ]:




