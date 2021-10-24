#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkIfNotNumeric(*args):
    for i in args:
        if not(isinstance(i,(int,float))):
            return False
    return True


# In[2]:


def addAllNumerics(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


# In[3]:


def searchNumFromList(L,n): # input L and the specific n you'd like to find
    matchNum = 0
    matchPlace = []
    for i in range(len(L)):
        if L[i] == n:
            matchNum += 1
            matchPlace =matchPlace + [i]
        else:
            pass

    print('Search ['+str(n)+'] in list ' + str(L))
    print('Match found in List: '+str(matchNum))
    print('Match place in List: ' + str(matchPlace) )


# In[5]:


def sortList(L):
    sL = [] # sorted list
    while len(L) > 0:
        sL.append(searchMinFromList(L)[0]) # add min value to sorted list
        L.remove(searchMinFromList(L)[0])# delete the min value from original list
        '''another way to do this could be
        minNum,idx = searchMinFromList(L)
        sL.append(minNum)
        del L(idx)
        '''
        
    return sL


def searchMinFromList(L):
    minValue = L[0]
    idx = 0
    for counter in range(len(L)):
        v=L[counter]
        if v < minValue:
            minValue = v
            idx = counter
        else:
            pass
            
    return minValue,idx


# In[ ]:




