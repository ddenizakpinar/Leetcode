# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1
        while left < right:
            max_area = max(max_area, abs(min(height[left], height[right]) * (left - right)))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area


height = [2, 3, 4, 5, 18, 17, 6]
s = Solution()
print(s.maxArea(height))
