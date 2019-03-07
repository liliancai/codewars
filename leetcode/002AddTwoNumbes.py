# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        root = result = ListNode(0)
        summary = 0 
        while (l1 or l2 or summary):
            if l1:
                summary += l1.val
                l1 = l1.next
            if l2:
                summary += l2.val
                l2 = l2.next
            result.next = ListNode( summary % 10)
            result = result.next
            summary //= 10
        return root.next
       
    
