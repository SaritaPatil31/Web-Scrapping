#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import requests 


# In[3]:


import numpy as np


# In[4]:


from bs4 import BeautifulSoup


# In[12]:


webpage=requests.get("https://www.ambitionbox.com/list-of-companies?page=1").text


# In[13]:


soup=BeautifulSoup(webpage,'lxml')


# In[15]:


print(soup.prettify())


# In[16]:


soup.find_all('h1')[0].text


# In[19]:


for i in soup.find_all('h2'):
    print(i.text.strip())


# In[31]:


len(soup.find_all('p',class_='rating'))


# In[32]:


company=soup.find_all('div',class_='company-content-wrapper')


# In[33]:


len(company)


# In[35]:


name


# In[48]:


name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
old=[]
employees=[]

for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('p').text.strip())
    reviews.append(i.find('a', class_='review-count').text.strip())
    ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    hq.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    old.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    employees.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    
d={'name':name,'rating':rating,'reviews':reviews,'type of Company':ctype,'headQuarter':hq,'Age of Company':old,'Employees':employees}
df=pd.DataFrame(d)
df


# In[67]:


final.shape


# In[82]:


final=pd.DataFrame()

for j in range(1,11):
    url=('https://www.ambitionbox.com/list-of-companies?page={}'.format(j))
    
    webpage=requests.get(url).text
    soup=BeautifulSoup(webpage,'lxml')
    company=soup.find_all('div',class_='company-content-wrapper')
    
    name=[]
    rating=[]
    reviews=[]
    ctype=[]
    hq=[]
    old=[]
    employees=[]

    for i in company:
        name.append(i.find('h2').text.strip())
        rating.append(i.find('p').text.strip())
        reviews.append(i.find('a', class_='review-count').text.strip())
        try:
            ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        except:
            ctype.append(np.nan)
        try:
            hq.append(i.find_all('p', class_='infoEntity')[1].text.strip())
        except:
            hq.append(np.nan)
        try:
            old.append(i.find_all('p', class_='infoEntity')[2].text.strip())
        except:
            old.append(np.nan)
        try:
            employees.append(i.find_all('p',class_='infoEntity')[3].text.strip())
        except:
            employees.append(np.nan)

        
    d={'name':name,'rating':rating,'reviews':reviews,'type of Company':ctype,'headQuarter':hq,'Age of Company':old,'Employees':employees}
    df=pd.DataFrame(d)
    
    final=final.append(df, ignore_index=True)


# In[83]:


final


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




