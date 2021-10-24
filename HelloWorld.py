#!/usr/bin/env python
# coding: utf-8

# # Hello World! 

# This is my first program using jupyter notebook!

# In[1]:


print('Hello World!')


# In[2]:


print("Hello World!")


# $a+b=42$

# using $ to use lattic to express math equation

# In[3]:


4+5


# In[4]:


85^3


# In[5]:


86*3


# # Variables

# In[6]:


x = 3


# In[10]:


get_ipython().run_line_magic('whos', '')
#this tells you the memories used in the program


# In[11]:


print(type(x))


# In[12]:


x=6.66


# In[13]:


get_ipython().run_line_magic('whos', '')


# In[14]:


print(type(x))


# In[15]:


y=5


# In[16]:


z=x*y


# In[17]:


get_ipython().run_line_magic('whos', '')


# In[18]:


a,b,c,d = 1,0.5,-3,4.0


# In[19]:


get_ipython().run_line_magic('whos', '')


# In[20]:


del b


# In[21]:


print(a,b,c,d)


# In[22]:


print(a,c,d)


# In[23]:


a=2+4j


# In[24]:


b=3-5j


# In[25]:


c=a+b


# In[26]:


c


# In[27]:


type(c)


# In[28]:


d='Hello World!'


# In[29]:


type(d)


# # Operators

# In[30]:


1+3 #addition


# In[31]:


3-2 #substraction


# In[32]:


9/3 #division


# In[33]:


3*3 #multiplication


# In[34]:


10%3 #reminder


# In[35]:


10//3 #floor division


# In[36]:


4**2 # to the power of 


# In[37]:


_ #underscore contains the last results that has been stored in a variable


# # Bool Type

# In[38]:


1 == 1


# In[39]:


2 >= 1


# In[40]:


2 > 3


# In[41]:


4 != 6


# In[42]:


type(True)


# In[43]:


type(False)


# In[ ]:




