#searchNumFromList
L=[23,-4,5,6,-10,100,-4] # sample list

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

    
searchNumFromList(L,-3) # test
