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


# In[2]:


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


A = np.arange(100) # generate an array from 0 to 99


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


# In[17]:


A = np.random.rand(100) # generate 100 random number


# In[18]:


print(A)


# In[19]:


get_ipython().run_line_magic('pinfo', 'np.random.rand')


# In[20]:


import matplotlib.pyplot as plt


# In[22]:


plt.hist(A,bins=100)


# In[24]:


get_ipython().run_line_magic('pinfo', 'np.random.randn')


# In[25]:


B = np.random.randn(10000)


# In[29]:


plt.hist(B,bins=200)


# In[30]:


D = np.arange(100).reshape(5,20) # reshape the array to required dimension


# In[31]:


D.shape


# In[32]:


print(D)


# In[1]:


# Slicing Array[start:end:step]


# In[3]:


A = np.arange(10)


# In[4]:


A


# In[5]:


A[1:5]


# In[6]:


A[0:5]


# In[7]:


A[:5] == A[0:5]


# In[8]:


B = A[3:7]


# In[9]:


B


# In[10]:


B[0] = -10


# In[11]:


B


# In[12]:


A


# In[13]:


'''
Array A and B points to the same reference (memory)
change A or B will affect each other
'''


# In[14]:


B = A[3:7].copy() 
# this will assign different memory to store Array


# In[15]:


B


# In[16]:


B[0]=3


# In[17]:


B


# In[18]:


A


# In[19]:


A[::-1]


# In[20]:


A[::-3]


# In[25]:


np.argwhere(A==-10) # return the index of the element


# In[31]:


np.argwhere(A==10)


# In[34]:


idx = np.argwhere(A==10)


# In[35]:


idx


# In[38]:


np.shape(idx)


# In[39]:


A[3]


# In[40]:


A = np.round(10*np.random.rand(5,4))


# In[41]:


A


# In[42]:


A[1,2]


# In[43]:


A[1,:]


# In[44]:


A[:,2]


# In[45]:


A[0:1,0:1]


# In[46]:


A[0:2,0:2]


# In[48]:


A[2:4,0:2]


# In[49]:


A


# In[54]:


A.sort(axis=0) # sort by column


# In[55]:


A


# In[56]:


A.sort(axis=1) # sort by row


# In[57]:


A


# In[58]:


# Numpy Indexing


# In[59]:


A


# In[60]:


A[A<6]


# In[61]:


A=np.arange(100)


# In[68]:


B=A[[3,5,6]] # double [[]] means copy rather than pointing to the same memory


# In[63]:


A


# In[64]:


B


# In[65]:


B[0]=-4


# In[66]:


B


# In[67]:


A


# In[69]:


B = A[A<40]


# In[70]:


B


# In[71]:


C = A[(A<40) & (A>30)]


# In[72]:


C


# In[73]:


# & for array, 'and' for single objects
# |, or
# ~, not


# In[74]:


# Broadcasting


# In[76]:


A = np.array([[1,2],[3,5]])


# In[77]:


A


# In[78]:


A = A+5


# In[79]:


A


# In[80]:


A = A + [1,2]


# In[81]:


A


# In[83]:


A = A + [[1],[2]]


# In[84]:


A


# In[86]:


# np.hstack horrizontal stack
# np.vstack vertical stack
# np.sort(axis = 0)


# In[87]:


A = np.round(10*np.random.rand(2,3))


# In[88]:


A


# In[89]:


B = np.round(20*np.random.rand(2,2))


# In[90]:


B


# In[95]:


C = np.hstack((A,B))


# In[96]:


C


# In[99]:


D = np.round(30*np.random.rand(5))


# In[100]:


D


# In[101]:


E = np.vstack((C,D))


# In[102]:


E


# In[103]:


# speed:ufuncs


# In[104]:


b = np.random.rand(1000000)


# In[105]:


get_ipython().run_line_magic('timeit', 'sum(b)')


# In[106]:


get_ipython().run_line_magic('timeit', 'np.sum(b) # same as B.sum()')


# In[107]:


# np.sum() is 100 times faster than sum()


# In[108]:


def mySum(G):
    s = 0
    for x in G:
        s+=x
    return s


# In[109]:


get_ipython().run_line_magic('timeit', 'mySum(b)')


# # Pandas

# In[113]:


import pandas as pd


# In[115]:


print(pd._version)


# In[116]:


pd.__version__


# In[117]:


A = pd.Series([2,3,4,5],index = ['a','b','c','d'])


# In[118]:


A.values


# In[120]:


type(A.values) # numpy array


# In[121]:


type(A) # pandas


# In[122]:


A.index


# In[123]:


A['a']


# In[124]:


A['a':'c'] # slicing using index


# In[125]:


# Series


# In[126]:


grade_dict = {'A':4,'A-':3.5,'B':3,'B-':2.5,'B':2}
grades = pd.Series(grade_dict)


# In[127]:


grades.values


# In[128]:


marks_dict = {'A':85,'B':75,'C':65,'D':55}
marks = pd.Series(marks_dict)


# In[129]:


marks


# In[130]:


marks['A']


# In[131]:


marks[:2]


# In[132]:


type(marks)


# In[133]:


grades # 'B' has been overwritten


# In[134]:


# DataFrame


# In[135]:


D = pd.DataFrame({'Marks':marks,'Grades':grades})


# In[136]:


D


# In[137]:


D.T


# In[138]:


D.values


# In[139]:


D.values[1,1]


# In[140]:


D.columns


# In[141]:


D


# In[142]:


D['ScaledMarks'] = D['Marks']*1.5


# In[143]:


D


# In[144]:


del D['ScaledMarks']


# In[145]:


D


# In[146]:


G = D[D['Marks']>70]


# In[147]:


G


# In[149]:


D.values[1,0]


# In[150]:


type(D.values[1,0])


# In[151]:


# NaN is float64?


# In[152]:


A = pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])


# In[153]:


A


# In[154]:


A.fillna(0) # fill nan with 0


# In[159]:


A.dropna


# In[160]:


A = pd.Series(['a','b','c'],index = [1,3,5])


# In[161]:


A[1] # explicit index, or loc


# In[163]:


A[1:3] # implict index, or iloc


# In[164]:


A.loc[1:3] # explicit index


# In[165]:


A.iloc[1:3] # implict index 


# In[166]:


D


# In[168]:


D.iloc[2,:]


# In[169]:


D.loc['A']


# In[170]:


D.iloc['A']


# In[171]:


# deal with csv files


# In[172]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


# In[173]:


df = pd.read_csv('/Users/yuanni/Documents/Python/covid_19_data.csv')


# In[174]:


df.head() # showing top 5 items by default


# In[175]:


df.drop(['SNo','Last Update'],axis=1,inplace=True)


# In[176]:


df.head()


# In[178]:


df.rename(columns={'ObservationDate':'Date','Province/State':'Province'},inplace=True)


# In[179]:


df.head()


# In[180]:


df['Date'] = pd.to_datetime(df['Date'])


# In[181]:


df.head()


# In[185]:


df.describe()


# In[186]:


df.info()


# In[189]:


df = df.fillna('NA')


# In[190]:


df.info()


# In[ ]:




