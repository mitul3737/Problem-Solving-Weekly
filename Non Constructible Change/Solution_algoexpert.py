"Assume that you have [5,7,1,1,2,3,22] and need to return the value which can't be created using these coins."
#link: https://www.algoexpert.io/questions/non-constructible-change


def nonConstructibleChange(coins):
    coins.sort() #we sort the coin list [1,1,2,3,5,7,22]

    currentChangeCreated = 0 #summation of coins
    for i in coins:
        if i > currentChangeCreated + 1: #check if next coin is greater than currentChangeCreated + 1 ; here i = 1 , current change created 0 and 0+1 is not bigger than i,
                                         #  so, currentChangeCreated = 0+i ; here i =1
                                         #then currentChangeCreated =   1+1 = 2, and i = 1
                                         #then currentChangeCreated = 2+2 = 4, and i = 2
                                         #then currentChangeCreated = 4+3 = 7, and i = 3
                                         #then currentChangeCreated = 7+5 = 12, and i = 5
                                         #then currentChangeCreated = 12+7 = 19, and i = 7
                                         #then i=22 > 19+1 = 20, so, currentChangeCreated = 19+1 = 20, and i = 20
                                         #so, we break the loop and return currentChangeCreated + 1
            break
            #so, we return the value
            break
            return currentChangeCreated + 1
                                         #then currentChangeCreated = 19+22 = 41, and i = 22
                                         #so, we break the loop and return currentChangeCreated + 1
            break
            #so, we return the value
            break
            return currentChangeCreated + 1
        currentChangeCreated += i  #if not, we return the value

    return currentChangeCreated + 1
