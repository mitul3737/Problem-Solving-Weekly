"""Two Number Sum - Algoexpert
https://www.algoexpert.io/questions/two-number-sum
"""
#solution 1 : Brute Force Approach
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        num_1=array[i]
        for j in range(i+1,len(array)):
            num_2=array[j]
            if num_1+num_2==targetSum:
                return [num_1,num_2]
    return []

# Time: O(n^2)
# Space: O(1)

#solution 2 : Hash Table Approach
def twoNumberSum(array, targetSum):
    hash_table={}
    for num in array:
        if targetSum-num in hash_table:
            return [targetSum-num,num]
        else:
            hash_table[num]=True
    return []

# Time: O(n)
# Space: O(n)

#solution 3 : Sorting Approach/Two Pointer Approach
def twoNumberSum(array, targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        currentSum=array[left]+array[right]
        if currentSum==targetSum:
            return [array[left],array[right]]
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right-=1
    return []

# Time: O(nlog(n))
# Space: O(1)



