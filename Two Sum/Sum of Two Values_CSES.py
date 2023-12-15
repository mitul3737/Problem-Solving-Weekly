"""Link: https://cses.fi/problemset/submit/1640/"""


#solution 1 : Brute Force Approach (Time Limit Exceeded)

"""len,sum=input().split(" ")
array=input().split(" ")

len=int(len)
sum=int(sum)

def twoSum(nums,target):
        x=True
        for i in range(len-1):

            num_1=int(nums[i]) #convert string to int
            for j in range(i+1,len):

                num_2=int(nums[j]) #convert string to int
                if num_1+num_2==target:
                    print(i+1, j+1)
                    x=False

        if x==True:       
            print("IMPOSSIBLE")

twoSum(array,sum)
"""
# Time: O(n^2)
# Space: O(1)

"""#Solution 2 : Hash Table Approach (Time Limit Exceeded)
len,sum=input().split(" ")
array=input().split(" ")

array=[int(i) for i in array] #convert string to int

len=int(len)
sum=int(sum)

def twoSum(nums, target):
        x=True
        hash_table = {}
        for num in range(len):
            #print(num)
            if target - int(nums[num]) in hash_table:
                print(nums.index(target-int(nums[num]))+1, num+1) #asked positions not index
                x=False
            else:
                hash_table[int(nums[num])] = num  # key is the number, value is the index 
                #print(hash_table)

        if x==True:
            print("IMPOSSIBLE")
twoSum(array,sum)"""


# Time: O(n)
# Space: O(n)

#solution 3 : Sorting Approach/Two Pointer Approach

len,sum=input().split(" ")
array=input().split(" ")

array_0=[int(i) for i in array] #convert string to int

array_1=[int(i) for i in array] #convert string to int and kept it to use it after sorting . Because after sorting the index will be changed

len=int(len)
sum=int(sum)

def twoNumberSum(array, targetSum):
    x=True
    array_0.sort()
    left=0
    right=len-1
    while left<right:
        currentSum=array_0[left]+array_0[right]
        if currentSum==targetSum:

            left_position=array_1.index(array_0[left])+1
            right_position=array_1.index(array_0[right])+1


            if left_position==right_position: #we do have isses dfor duplicate values
                right_position=array_1.index(array_0[right],left_position)+1
             
            print(left_position,right_position)
            


            x=False
            break
        elif currentSum<targetSum:
            left+=1
        elif currentSum>targetSum:
            right-=1
    if x==True:
        print("IMPOSSIBLE")

twoNumberSum(array,sum)

# Time: O(nlog(n))
# Space: O(1)