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


# In[1]:


a=True
b=True
c=False


# In[2]:


get_ipython().run_line_magic('whos', '')


# In[3]:


a and b
a and c
b and c


# In[4]:


print(a and b)
print(a and c)
Print(b and c)


# In[5]:


print(a and b)
print(a and c)
print(b and c)


# In[6]:


print(a or b)
print(a or c)
print(c or b)


# In[7]:


not(a)


# In[8]:


not(c)


# In[9]:


not(a and b)


# In[10]:


print((not(2!=3) and True) or (True and False) )


# In[11]:


divmod(27,5)


# # Some Useful Functions

# In[12]:


round(4.5)


# In[13]:


round(4.51)


# In[14]:


round(4.55555,3)


# In[15]:


divmod(27,5)


# In[16]:


divmod(28,4)


# In[17]:


type(divmod(28,4))


# In[18]:


g = divmod(15,4)


# In[19]:


g[0]


# In[20]:


g[1]


# In[21]:


print(isinstance(1,int))


# In[22]:


print(isinstance(1.0,int))


# In[23]:


print(isinstance(1.0,(int,float))


# In[24]:


print(isinstance(1.0,(int,float)))


# In[25]:


pow(3,2)


# In[26]:


pow(3,2,2) #equals 3^2%2


# In[27]:


a = int(input('Please enter an integar: '))


# In[28]:


type(a)


# In[29]:


b = input('Please enter an integar: ')


# In[30]:


type(b)


# In[31]:


print? # add a ? after a func will display how to use it 


# In[32]:


help(print)


# # Functions

# In[1]:


def sampleFunc(a=0)
    return a


# In[14]:


def sampleFunc(a=0): # sets a default 
    return a


# In[15]:


sampleFunc()


# In[16]:


sampleFunc(1)


# In[5]:


def sampleFunc2(*a): # this allows multiple inputs
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum


# In[6]:


sampleFunc2(2,3,4)


# In[7]:


sampleFunc2(2,3,4,5,6,7)


# In[9]:


sampleFunc2(8)


# In[8]:


sampleFunc2(2,3.7,4.0)


# In[12]:


def printVV(**a): #this allows to print all the keys and values
    for i in a:
        print('Variable is ',i,', and the value is ',a[i])


# In[13]:


printVV(a=4,b='N',c=4.6,d=2+3j)


# In[17]:


def printList(L=[1,2,3]):
    print(L)


# In[18]:


printList()


# In[19]:


L2=[0,9,4,6,-12]
printList(L2)


# In[20]:


printList(L3=[4,5,6])


# In[21]:


printList(L=[4,5,6])


# In[22]:


help(printList())


# # Modules

# In[1]:


import sys
sys.path.append('/Users/yuanni/Documents/Python/myModules/')
# add Modules folder to the path


# In[2]:


import MyUniversalFunctions as myfs
#import modules and name them


# In[3]:


get_ipython().run_line_magic('pinfo', 'myfs.addAllNumerics')


# In[4]:


myfs.addAllNumerics(1,3,5,7,9)


# In[5]:


help(myfs.addAllNumerics)


# In[6]:


from MyUniversalFunctions import addAllNumerics


# In[7]:


addAllNumerics(2,3,4,6,8)


# In[8]:


def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


# In[9]:


L = [2,3,6,7]


# In[10]:


L2 = swapValues(L,1,3)


# In[11]:


print(L2)


# In[14]:


myfs.sortList(L)


# In[15]:


help(myfs.sortList)


# In[16]:


a = 'string'


# In[21]:


b=a.capitalize()


# In[23]:


b


# In[24]:


c=a.replace('i','3')


# In[25]:


c


# # Data Structure

# In[2]:


pip install jupyterthemes


# In[3]:


jt -l


# In[1]:


L = [1,3,5,7] # list
T = (1,3,5,7) # tuple
S = {1,3,5,7} # set
D = {1:'one',3:'three',5:'five',7:'seven'} # dictionary


# In[2]:


print(type(L))
print(type(T))
print(type(S))
print(type(D))


# In[3]:


L[1]


# In[4]:


T(1)


# In[5]:


T[1]


# In[6]:


print(L[2])
print(T[2])
print(5 in S)
print(D[5])


# In[7]:


D1 = {2:'two',4:'four',6:'six',8:'eight'}


# In[8]:


D2 = D1+D2


# In[9]:


D2 = D.update(D1)


# In[10]:


D2


# In[11]:


D


# In[12]:


D.sort()


# In[13]:


D.keys()


# In[14]:


L


# In[15]:


L1 = L


# In[16]:


L1


# In[17]:


L1[1]=4


# In[18]:


L1 # L and L1 reference to the same memory


# In[19]:


L


# In[20]:


L2 = L.copy() 
# L2 and L reference to different memory using .copy()


# In[21]:


L2


# In[22]:


L2[1] = 3


# In[23]:


L2


# In[24]:


L


# In[25]:


# slicing a list returns a copy (Numpy is different)


# In[26]:


L3 = [x**2 for x in range(10)]


# In[27]:


L3


# # Numpy

# In[3]:


'''Why Numpy? Numpy is Faster''' 


# In[3]:


import numpy as np


# In[5]:


a = np.array([1,2,3,4,5])
b = np.array((1,6,3,4,9))


# In[6]:


print(a,b)


# In[7]:


print(a)


# In[8]:


print(b)


# In[9]:


type(a)


# In[10]:


type(b)


# In[12]:


a.dtype


# In[13]:


c = np.array([1,3,5,7],dtype='f')


# In[14]:


c


# In[16]:


c.dtype # data type


# In[18]:


a = np.array([[1,2,3],[4,5,6]])


# In[19]:


print(a.ndim) # dim stands for dimension


# In[20]:


a[1]


# In[21]:


a[0]


# In[22]:


b = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])


# In[23]:


print(b.ndim)


# In[24]:


print(b.shape[0],b.shape[1],b.shape[2])


# In[25]:


print(b[1,0,2])


# In[1]:


'''
np.arange
np.random.permutation
np.reshape
'''


# In[4]:


A = np.arange(100)


# In[5]:


A


# In[6]:


print(A)


# In[7]:


B = np.arange(20,100)


# In[8]:


print(B)


# In[9]:


C = np.arange(20,100,3) # (start, end, step)


# In[10]:


print(C)


# In[11]:


A = np.random.permutation(np.arange(10))


# In[12]:


print(A)


# In[13]:


V = np.random.randint(0,10)


# In[14]:


print(V)


# In[15]:


np.random.randint(0,10)


# In[16]:


np.random.randint(0,10)


# In[ ]:




