"""Leetcode
https://leetcode.com/problems/two-sum/description/
"""

#solution 1 : Brute Force Approach
class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        for i in range(len(nums)-1):
            #print(nums[i])
            num_1=nums[i]
            for j in range(i+1,len(nums)):
                num_2=nums[j]
                if num_1+num_2==target:
                    return [i,j]
        return []
    
# Time: O(n^2)
# Space: O(1)

#solution 2 : Hash Table Approach
class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for num in range(len(nums)):
            print(num)
            if target - nums[num] in hash_table:
                return [nums.index(target-nums[num]), num]
            else:
                hash_table[nums[num]] = num  # key is the number, value is the index 
        return []
    
# Time: O(n)
# Space: O(n)



