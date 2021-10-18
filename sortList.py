# sortList
# sort numbers in a list from low to high

L = [23,10,9,-3,400,-10,0,3,-3]

def sortList(L):
    sL = [] # sorted list
    while len(L) > 0:
        sL.append(searchMinFromList(L)[0]) # add min value to sorted list
        L.remove(searchMinFromList(L)[0])# delete the min value from original list
        
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
            
    return minValue,counter

print(sortList(L)) #test

