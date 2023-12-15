#https://www.algoexpert.io/questions/sorted-squared-array

def sortedSquaredArray(array):
     for index in range(len(array)): #O(n)
         array[index]= array[index]*array[index]
     array.sort() #sort the values #O(nlogn))
     return array

#solution 2

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares
# Time Complexity: O(n)
# Space Complexity: O(n)


#solution 3 (new place to store the values)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value
    sortedSquares.sort()
    return sortedSquares

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

 
