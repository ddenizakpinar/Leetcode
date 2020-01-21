# https://leetcode.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur, arr = head, []

        while cur is not None:
            arr.append(cur.val)
            cur = cur.next

        return arr == arr[::-1]


root = ListNode(1)
root.next = ListNode(3)

s = Solution()
print(s.isPalindrome(root))
