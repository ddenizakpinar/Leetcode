# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            max(prices[::])
    
s = Solution()
arr = [7,1,5,3,6,4]
print(s.maxProfit(arr))
