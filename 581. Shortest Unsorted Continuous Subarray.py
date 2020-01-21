# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        if (nums == sortedNums):
            return 0
        for i in range(0,len(nums)-1):
            if sortedNums[i] != nums[i]:
                start = i
                break

        for i in range(len(nums)-1,0,-1):
            if sortedNums[i] != nums[i]:
                return (i-start)+1

input = [ 1,2]
s = Solution()
print(s.findUnsortedSubarray(input))
