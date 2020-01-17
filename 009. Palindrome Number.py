# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list = []
        while int(x) > 0:
            list.append(x % 10)
            x = int(x / 10)
        if list == list[::-1]:
            return True
        return False


s = Solution()
print(s.isPalindrome(121))
