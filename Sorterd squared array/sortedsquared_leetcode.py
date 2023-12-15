#Link: https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, array: List[int]) -> List[int]:
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