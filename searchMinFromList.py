#searchMinFromList.py

def searchMinFromList(L):
    minValue = L[0]
    for counter in range(len(L)):
        v=L[counter]
        if v < minValue:
            minValue = v
        else:
            pass
            
    return minValue
    print(minValue)
