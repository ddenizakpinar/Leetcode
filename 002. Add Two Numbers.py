# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2 = [], []
        while l1 is not None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            list2.append(l2.val)
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        s1 = ''
        s2 = ''
        for i in list1:
            s1 = s1 + str(i)
        for i in list2:
            s2 = s2 + str(i)

        summary = int(s1) + int(s2)
        stringSummary = str(summary)[::-1]
        root, temp = None, None

        for i in stringSummary:
            if root is None:
                root = ListNode(i)
                temp = root
            else:
                temp.next = ListNode(i)
                temp = temp.next

        return root


c = Solution()
l1 = ListNode(5)
l2 = ListNode(5)
root = c.addTwoNumbers(l1, l2)
