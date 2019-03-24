# 44 ms, faster than 85.05% of Python3, E

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2 # unessary but
        root = result = ListNode(0)
        while p1 and p2:    
            if p1.val < p2.val:
                result.next = p1
                p1 = p1.next
            else:
                result.next = p2
                p2 = p2.next
            result = result.next
        result.next = p1 or p2
        return root.next
