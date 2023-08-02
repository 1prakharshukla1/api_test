#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests


# In[29]:


headers={'access_token': 'fe66583bfe5185048c66571293e0d358'}
api_endpoint='https://zucwflxqsxrsmwseehqvjmnx2u0cdigp.lambda-url.ap-south-1.on.aws/mentorskool/v1/sales'


# In[37]:


try:
    response=requests.get(api_endpoint,headers=headers)
    response.raise_for_status()
    data = response.json()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
except Exception as e:
    print(f'un-identified : {e}')


# In[39]:


response.json()


# In[ ]:



 


# In[ ]:




