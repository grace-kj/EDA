#!/usr/bin/env python
# coding: utf-8

# In[2]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))


# In[3]:


from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeListInDong'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '/vbtYcG/rbjqTvfo+uB6Wo9W2CvXXIKLIct9B+ij/pmSvYoZIoPySQSN+7+2tZeTOagErsaoSh1Xpy8AXLy5TQ==',
                               quote_plus('pageNo') : '1', quote_plus('numOfRows') : '100',\
                              quote_plus('divId') : 'ctprvnCd', quote_plus('key'): '11', quote_plus('indsLclsCd'): 'Q', \
                              quote_plus('indsMclsCd'): 'Q12', quote_plus('indsSclsCd'): 'Q12A01', quote_plus('type'): 'json'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print (response_body)


# In[ ]:





# In[ ]:




