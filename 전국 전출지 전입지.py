#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import os
import pandas as pd

#다운받은 csv 불러오기

df= pd.read_csv("C:\\PycharmProjects\\bigdata\\Data\\전출지_전입지_시도_별_이동자수_2021.csv",engine='python', sep=',')

print(df.columns)


# In[3]:


df.head()


# In[4]:





# In[ ]:




